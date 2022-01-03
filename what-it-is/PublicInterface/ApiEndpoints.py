
from flask import Flask
from flask_restful import Api

from PublicInterface.RESTModels.Cryptos import Cryptos
from PublicInterface.RESTModels.CryptosAndPrices import CryptosAndPrices
from PublicInterface.RESTModels.ExampleWithParametersAndRequestBody import ExampleWithParametersAndRequestBody

class ApiEndpoints:

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(Cryptos, self.create_path_for_endpoint('cryptos'))
        self.api.add_resource(CryptosAndPrices, '/api/get-prices')
        self.api.add_resource(ExampleWithParametersAndRequestBody, '/api/example/<string:name>/<int:age>')

        self.app.run(debug=True)


    def create_path_for_endpoint(self, hook):
        return '/api/' + hook