from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import config

class TwitterListener(StreamListener):

    def on_data(self, data):
        print data
        # print json.dumps(data, sort_keys=True,indent=4,separators=(',', ': '))
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    twitter_listener = TwitterListener()

    auth = OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, twitter_listener)

    stream.filter(track=['python', 'javascript', 'ruby'])
