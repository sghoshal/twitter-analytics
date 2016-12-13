import tweepy
import json, string, jsonpickle
import config

from pprint import pprint

class TwitterListener(tweepy.StreamListener):

    def __init__(self, proxyUrl=None, producer=None):
        super(TwitterListener, self).__init__()
        self.producer = producer

    def on_status(self, status):

        print ""
        print "###################################################"
        print "#################    NEW TWEET    #################"
        print "###################################################"
        print ""

        # The status object converted to JSON
        # status_json = jsonpickle.encode(status)
        # print status_json

        # Create a comma separated string of all mentions in the tweet.
        mentions = ",".join(str(m['screen_name']) for m in status.entities['user_mentions'])

        # Send only relevant attributes from the Status object.
        # text, lang, user_twitter_handle, followers_count, retweet_count, source, location, timezone, mentions
        message = "%s||%s||%s||%s||%s||%s||%s||%s||%s" % \
                    (status.text, status.lang, status.user.screen_name, 
                        status.user.followers_count, 
                        status.retweeted_status.retweet_count if hasattr(status, 'retweeted_status') else 0, 
                        status.source, status.author.location, status.author.time_zone, mentions)

        msg = filter(lambda x: x in string.printable, message)
        self.producer.sendMessage(msg)

        return True

    def on_error(self, status):
        print status