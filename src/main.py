import tweepy
import time
import config, auth_keys

from twitter_listener import TwitterListener
from kafka_producer import AppKafkaProducer
from kafka_consumer import AppKafkaConsumer

if __name__ == '__main__':
    # Create the Kafka Producer
    producer = AppKafkaProducer()

    # Set up the Twitter listener.
    twitter_listener = TwitterListener(producer=producer)

    auth = tweepy.OAuthHandler(auth_keys.CONSUMER_KEY, auth_keys.CONSUMER_SECRET)
    auth.set_access_token(auth_keys.ACCESS_TOKEN, auth_keys.ACCESS_TOKEN_SECRET)

    stream = tweepy.streaming.Stream(auth, twitter_listener)

    # Start the Kafka Consumer on a separate thread.
    consumer = AppKafkaConsumer()
    consumer.start()
    
    time.sleep(10)
    
    # Start listening for tweets on the stream.
    stream.filter(track=['arsenal'])