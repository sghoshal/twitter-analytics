import threading
import config

from kafka import KafkaConsumer

class TwitterConsumer(threading.Thread):
    daemon = True

    def run(self):
        # When a new consumer subscribes to a particular topic, and there have already been few messages published on that topic,
        # we want the consumer to receive messages from the earliest Kafka knows of. 
        # (The Kafka log retention policy will determine the earliest one)
        # SO http://stackoverflow.com/questions/32390265/what-determines-kafka-consumer-offset

        consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='smallest')
        consumer.subscribe([config.TOPIC])

        for message in consumer:
            print "---------- CONSUMER: ", message