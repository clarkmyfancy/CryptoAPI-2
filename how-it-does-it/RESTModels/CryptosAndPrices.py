from flask_restful import Resource, reqparse

from DataBridge.DataBridge import getCryptosOfInterest
from CoinMarketCapApi.Api import Api



class CryptosAndPrices(Resource):

    def get(self):
        api = Api()
        cryptos = getCryptosOfInterest()
        cryptos_with_prices = api.getQuotes(cryptos)
        results = list(cryptos_with_prices)
        return { 'data': results}, 200