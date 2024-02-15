#we will be using coincap api to get the crypto data

import requests

#endpoint for market data
url = "https://api.coincap.io/v2/assets"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)