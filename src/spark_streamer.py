# To run this script, the spark streaming JAR needs to be included in the classpath.
# spark-submit --jars ..\lib\spark-streaming-kafka-0-8-assembly_2.11-2.0.2.jar .\spark_streamer.py
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

import config

sc = SparkContext(appName="KafkaSparkStreamer")
ssc = StreamingContext(sc, config.BATCH_INTERVAL)

stream = KafkaUtils.createDirectStream(ssc, [config.TOPIC], {"metadata.broker.list": config.KAFKA_SERVER})

lines = stream.map(lambda x: x[1])
lines.pprint()

counts = lines.flatMap(lambda line: line.split(" ")) \
            .map(lambda word: (word, 1)) \
            .reduceByKeyAndWindow(lambda a, b: (a + b), lambda x, y: x - y, config.WINDOW_SIZE, config.SLIDE_INTERVAL)

counts.pprint(num=50)

# Metadata checkpointing is primarily needed for recovery from driver failures, 
# whereas data or RDD checkpointing is necessary even for basic functioning if stateful transformations are used.
# http://spark.apache.org/docs/latest/streaming-programming-guide.html#checkpointing
ssc.checkpoint("D:\spark-stream-checkpoint")
ssc.start()
ssc.awaitTermination()