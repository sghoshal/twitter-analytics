# To run this script, the spark streaming JAR needs to be included in the classpath.
# spark-submit --jars ..\lib\spark-streaming-kafka-0-8-assembly_2.11-2.0.2.jar .\spark_streamer.py

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

import config

sc = SparkContext(appName="KafkaSparkStreamer")
ssc = StreamingContext(sc, config.BATCH_INTERVAL)

def extract_location(line):
    tokens = line.split("||")
    return str(tokens[6])

def extract_mentions(line):
    tokens = line.split("||")

    # Return a list of tuples where each tuple is the mentioned user with retweet count.
    retweet_count = int(tokens[4]) if tokens[4] != '0' else 1
    return [('@' + str(user), retweet_count) for user in tokens[8].split(',')]

def sort_by_value(rdd):
    flipped = rdd.map(lambda (x, y): (y, x))
    flipped_sorted = flipped.sortByKey(False)
    return flipped_sorted.map(lambda (x, y): (y, x))

stream = KafkaUtils.createDirectStream(ssc, [config.TOPIC], {"metadata.broker.list": config.KAFKA_SERVER})

lines = stream.map(lambda x: x[1])
# lines.pprint()

# Reduce by author's timezone and effective user mentions over a sliding window.
tweet_locations = lines.map(extract_location).filter(lambda loc: loc != 'None').map(lambda x: (x, 1))
tweet_mentions = lines.flatMap(extract_mentions).filter(lambda user: user[0])
          
locations_agg = tweet_locations \
                .reduceByKeyAndWindow(lambda a, b: (a + b), lambda x, y: x - y, config.WINDOW_SIZE, config.SLIDE_INTERVAL) \
                .transform(lambda rdd: sort_by_value(rdd))

mentions_agg = tweet_mentions \
                .reduceByKeyAndWindow(lambda a, b: (a + b), lambda x, y: x - y, config.WINDOW_SIZE, config.SLIDE_INTERVAL) \
                .transform(lambda rdd: sort_by_value(rdd))

locations_agg.pprint()
mentions_agg.pprint()

# Metadata checkpointing is primarily needed for recovery from driver failures, 
# whereas data or RDD checkpointing is necessary even for basic functioning if stateful transformations are used.
# http://spark.apache.org/docs/latest/streaming-programming-guide.html#checkpointing
ssc.checkpoint("D:\spark-stream-checkpoint")
ssc.start()
ssc.awaitTermination()