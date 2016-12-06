import config

from kafka.producer import KafkaProducer

class TwitterProducer():
    
    def __init__(self):

        # Initialize Kafka.
        self.producer = KafkaProducer(bootstrap_servers=config.KAFKA_SERVER)

    def sendMessage(self, msg):
        self.producer.send(config.TOPIC, bytes(msg))
