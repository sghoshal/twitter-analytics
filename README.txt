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

