#we will be using coincap api to get the crypto data

import requests
import logging as log
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json



#defininf constants for kafka
CONS_KAFKA_SERVER = "localhost:29092"
CONS_KAFKA_TOPIC = "coincapData"

# Define the base URL for the CoinCap API
base_url = "https://api.coincap.io/v2/assets/"

# List of top 20 cryptocurrencies by market cap (example)
top_cryptos = ['bitcoin', 'ethereum', 'binancecoin', 'cardano', 'polkadot', 'chainlink', 'uniswap', 'solana', 'avalanche-2', 'ripple', 
               'dogecoin', 'litecoin', 'polygon', 'stellar', 'vechain', 'tezos', 'cosmos', 'algorand', 'ftx-token', 'elrond', 'aave']


def getDataCoinCap():
    #getting the market data from the api
    url = "https://api.coincap.io/v2/assets"
    payload = {}
    headers = {}
    print("Extracting data. Please wait......")
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def sendToKafka(alldata):
    #kafka producer for pushing coincap response into kafka topic
    producer = KafkaProducer(bootstrap_servers=CONS_KAFKA_SERVER, max_request_size=18485760)
    message = json.dumps(str(alldata))
    producerResponse = producer.send(CONS_KAFKA_TOPIC, message.encode('ascii'))

    #synchronous send code block
    try:
        record_metadata = producerResponse.get(timeout=10)
    except KafkaError:
        log.exception(KafkaError)
        pass
    
    print("Topic: ",record_metadata.topic)
    print("Partition: ",record_metadata.partition)





def fetchHistoricalData(crypto, interval='d1'):
    url = f"{base_url}{crypto}/history?interval={interval}"
    response = requests.get(url)
    data = response.json()
    return data



if __name__ == "__main__":
    #returnedResponse = fetchHistoricalData()
    print("Data extracted successfully!!!!")
    print("Posting to kafka.....")
    all_data = {}
    for crypto in top_cryptos:
        all_data[crypto] = fetchHistoricalData(crypto, interval='d1') # Assuming 'h1' for hourly data


    sendToKafka(all_data)

    







