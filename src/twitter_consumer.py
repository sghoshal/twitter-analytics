import threading
import config

from kafka import KafkaConsumer

class TwitterConsumer(threading.Thread):
    daemon = True

    def run(self):
        # Set auto_offset_reset='smallest' so the consumer gets messages from the beginning Kafka knows of
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='smallest')
        consumer.subscribe([config.TOPIC])

        for message in consumer:
            print "---------- IN CONSUMER | RECEIVED: ", message.value