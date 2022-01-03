import json

def getApiKeySecrets():
    file = open("HowItDoesIt/CoinMarketCapApi/secrets.json", "r")
    secrets = json.load(file)
    file.close()
    return secrets["api-key"]

def getCryptosOfInterest():
    file = open("WhatItIs/Database/CryptosOfInterest.txt", "r")
    cryptos = file.read()
    file.close()
    return cryptos

def addToCryptosOfInterest(ticker):
    file = open("WhatItIs/Database/CryptosOfInterest.txt", "a")
    thing = str(',' + ticker)
    file.write(thing)
    file.close()