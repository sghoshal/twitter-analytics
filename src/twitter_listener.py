import tweepy
import json, string
import config

from pprint import pprint

class TwitterListener(tweepy.StreamListener):

    def __init__(self, proxyUrl=None, producer=None):
        self.producer = producer
        api = tweepy.API(proxy=proxyUrl) if proxyUrl else tweepy.API()

        # print "ProxyURL #passed %s | Tweepy API object initialized to %s," % (proxyUrl, api)
        super(TwitterListener, self).__init__(api)

    def on_status(self, status):

        print ""
        print "###################################################"
        print "#################    NEW TWEET    #################"
        print "###################################################"
        print ""

        # pprint(vars(status))

        message = status.text + ',' + status.user.screen_name
        msg = filter(lambda x: x in string.printable, message)

        print msg

        # Send the msg in bytes to the broker using the producer.
        self.producer.sendMessage(msg)

        return True

    def on_error(self, status):
        print status

