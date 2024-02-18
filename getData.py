#we will be using coincap api to get the crypto data

import requests
import kafka
import logging as log
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json


#getting the market data from the api
url = "https://api.coincap.io/v2/assets"
payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)


#defininf constants for kafka
CONS_KAFKA_SERVER = "localhost:29092"
CONS_KAFKA_TOPIC = "coincapData"

#kafka producer for pushing coincap response into kafka topic


#Steps to sending api data to kafka topic
#1. getting the data... this step is completed and the data is in response
#2. creating a kafka topic...  this step is embedded in the 3rd step as producer will create the topic automatically if it doesn't exist
#3. sending data to kafka topic.. this is the final step and goes like this


producer = KafkaProducer(bootstrap_servers=CONS_KAFKA_SERVER)
message = json.dumps(response.text)
producerResponse = producer.send(CONS_KAFKA_TOPIC, message.encode('ascii'))


try:
    record_metadata = producerResponse.get(timeout=10)
except KafkaError:
    log.exception()
    pass


print(record_metadata.topic)
print(record_metadata.partition)





