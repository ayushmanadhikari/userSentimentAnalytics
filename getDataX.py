import requests
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError



#getting API key and secret key from apikey file
file = open('./apikey', 'r')
content = file.readlines()
apiKey = content[-4]
apiKeySecret = content[-1]
file.close()


twitterKeys = {
    "apikey": apiKey,
    "apiKeySecret": apiKeySecret
}




