import requests
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
import tweepy



#getting API key and secret key from apikey file
file = open('./apikey', 'r')
content = file.readlines()
consumerKey = content[13].strip()
consumerSecret = content[16].strip()
accessKey = content[6].strip()
accessSecret = content[9].strip()

keysList = [consumerKey, consumerSecret, accessKey, accessSecret]
for key in keysList:
    print(key)

file.close()


"""twitterKeys = {
    "apikey": consumerKey,
    "apiKeySecret": consumerSecret,
    "accessKey": accessKey,
    "accessSecret": accessSecret
}
"""


auth = tweepy.OAuth1UserHandler(
    consumerKey, consumerSecret, accessKey, accessSecret
)

api = tweepy.API(auth)

publicTweets = api.home_timeline()
for tweet in publicTweets:
    print(tweet.text)



