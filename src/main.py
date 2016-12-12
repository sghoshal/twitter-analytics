import tweepy
import time
import config

from twitter_listener import TwitterListener
from twitter_producer import TwitterProducer
from twitter_consumer import TwitterConsumer

if __name__ == '__main__':
    # Create the Kafka Producer
    producer = TwitterProducer()

    # Set up the Twitter listener.
    twitter_listener = TwitterListener(proxyUrl=None, producer=producer)

    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

    stream = tweepy.streaming.Stream(auth, twitter_listener)

    # Start the Kafka Consumer
    consumer = TwitterConsumer()
    consumer.start()
    time.sleep(10)
    
    # Start listening for tweets on the stream.
    stream.filter(track=['barcelona'])