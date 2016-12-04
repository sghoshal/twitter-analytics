STEPS:

Set up Kafka:

- Followed the official docs
- https://kafka.apache.org/quickstart
- Kafka important concept about Partitions, Consumers and Consumer Groups: 
    https://www.tutorialspoint.com/apache_kafka/apache_kafka_workflow.htm
- (If you are running on Windows, use Powershell to get over the convoluted windows bash syntax). I didn't want to spend a lot of time to get it to work on GitBash/MinGW.

Try out Twitter's Streaming API:

- Followed the first part of this tutorial - http://adilmoujahid.com/posts/2014/07/twitter-analytics/
    - Created a Twitter app on https://apps.twitter.com/app/
    - Got the Consumer API and Consumer secret
    - Generated the Access Token and Access Token secret (the generated tokens are only useful for making API requests on my account's behalf)
    - Install tweepy python client (pip install tweepy)
    - Referred to the tweepy docs - http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html

Notes:
1. Is there rate limiting with the Twitter Streaming API?
    - Rate limiting is applicable to the REST API. For streaming API, twitter returns about 1% of the total tweets being tweeted at the moment. 

    Reference:     https://twittercommunity.com/t/is-there-a-limit-to-the-amount-of-data-the-streaming-api-will-send-out/8482
    
    Whether you'll be streamed all the events matching those terms or not is determined by the relative volume of tweets matching those terms to the total volume of public tweets in the Firehose. The basic levels allow you to be streamed up to 1% of the total volume. Whether 30,000 people using those hashtags would result in going over 1% of the total firehose at any one moment of time or not is not necessarily determinate before the fact. You can find out some of our recent public numbers of how many tweets happen in the Firehose and try to make some estimates based on your projections.

