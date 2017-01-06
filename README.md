- This Python app streams tweets using Twitter's Streaming API and dispatches to a Kafka Producer.
- A separate Spark job performs aggregations like Tweets by location and effective user mentions in real time over a
sliding window. This is done using the Spark Streaming API.

---

## Setup

### Kafka
    - Docs https://kafka.apache.org/quickstart.
    - tar the tgz file.
    - Create an env variable KAFKA_HOME in ~/.bashrc and point it to the extracted directory.
    - Add $KAFKA_HOME/bin to the $PATH.
    - In $KAFKA_HOME/config/server.properties, add / uncomment
        `advertisers.listeners=PLAINTEXT://localhost:9092`

### Twitter Streaming API
    - Followed the first part of this tutorial - http://adilmoujahid.com/posts/2014/07/twitter-analytics/
        - Created a Twitter app on https://apps.twitter.com/app/
        - Got the Consumer API and Consumer secret
        - Generated the Access Token and Access Token secret (the generated tokens are only useful for making API requests on logged in user account's behalf)
        - Install tweepy python client (pip install tweepy)
        - Referred to the tweepy docs - http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html

### Spark
    - Download from http://spark.apache.org/downloads.html
    - Create env variable and add to path.

---

## STEPS TO RUN

### Kafka
    - Start Zookeeper.
    - Start Kafka Broker/Server.
    - Make sure the desired topic name in config.py is created first. If not, create the topic by running:

    `kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic <topic_name>`

    - Optional - Start the consumer to see what's being streamed.

### Tokens
- Generate all tokens from apps.twitter.com/app and paste the values to src/auth_keys.py. It should look like this:
    `ACCESS_TOKEN = xxx`
    `ACCESS_TOKEN_SECRET = xxx`
    `CONSUMER_KEY = xxx`
    `CONSUMER_SECRET = xxx`

### Dependencies
- Use pip:
    - sudo pip install tweepy --ignore-installed six
        - The package 'six' is already installed by Apple - https://github.com/pypa/pip/issues/3165
    - sudo pip install kafka-python

### Running the scripts
- In main.py, edit the track array to tweets containing the desired words.

- python src/main.py

- spark-submit --jars lib/spark-streaming-kafka-0-8-assembly_2.11-2.0.2.jar src/spark_streamer.py

---

## Concepts

### Kafka
    - Kafka important concept about Partitions, Consumers and Consumer Groups:
      - https://www.tutorialspoint.com/apache_kafka/apache_kafka_workflow.htm

    - What are offsets?
      - For each topic, the Kafka cluster maintains a partitioned log.
        Each partition is an ordered, immutable sequence of records that is continually appended to—a structured commit log. The records in the partitions are each assigned a sequential id number called the offset that uniquely identifies each record within the partition.

        https://kafka.apache.org/documentation (Section: Topics And Logs)

    - When there are more consumers than partitions:
        - New consumers don't get any messages because each Kafka consumer is assigned only a single partition.
          If a consumer dies/unsubscribes and if num consumers < partition, the new consumer will start receiving messages.
        - http://spark.apache.org/docs/latest/streaming-programming-guide.html#setting-the-right-batch-interval
        -
    - When Kafka Partitions outnumber consumers
        http://stackoverflow.com/questions/21293937/apache-kafka-message-consumption-when-partitions-outnumber-consumers

    - What is auto_offset_reset='smallest' in consumer config?

        When a new consumer subscribes to a particular topic, and there have already been few messages published on that topic,
        we want the consumer to receive messages from the earliest Kafka knows of.
        (The Kafka log retention policy will determine the earliest one)
        SO http://stackoverflow.com/questions/32390265/what-determines-kafka-consumer-offset

### Spark Streaming
    - What is the difference between batch interval and window?
        - The data collected in batch interval time becomes a RDD in spark (called the batch here).
        - The window is a collection of batches over the window time interval.
        - http://www.infoobjects.com/spark-streaming-window-vs-batch/
        - https://www.youtube.com/watch?v=NHfggxItokg&t=1559s 12min

    - Why do we need both batch interval and window if we can increase the batch interval?
        - This is useful for spark applications that need to both stream ingestion (real time event monitoring) as well as Aggregations over the window time period. If the use case is just to do aggregations, a high batch interval would be more efficient.

### Twitter Streaming API
    - Is there rate limiting with the Twitter Streaming API?
        - Rate limiting is applicable to the REST API. For streaming API, twitter returns about 1% of the total tweets being tweeted at the moment. 

        Reference:     https://twittercommunity.com/t/is-there-a-limit-to-the-amount-of-data-the-streaming-api-will-send-out/8482
        
        "Whether you'll be streamed all the events matching those terms or not is determined by the relative volume of tweets matching those terms to the total volume of public tweets in the Firehose. The basic levels allow you to be streamed up to 1% of the total volume. Whether 30,000 people using those hashtags would result in going over 1% of the total firehose at any one moment of time or not is not necessarily determinate before the fact. You can find out some of our recent public numbers of how many tweets happen in the Firehose and try to make some estimates based on your projections."

