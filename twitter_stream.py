import tweepy
import json
import config

class TwitterListener(tweepy.StreamListener):

    def on_status(self, status):
        print status
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    twitter_listener = TwitterListener()

    auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

    stream = tweepy.streaming.Stream(auth, twitter_listener)

    stream.filter(track=['python', 'javascript', 'ruby'])
