
from flask import Flask
from flask_restful import Api

from HowItDoesIt.RESTModels.Cryptos import Cryptos
from HowItDoesIt.RESTModels.CryptosAndPrices import CryptosAndPrices
from HowItDoesIt.RESTModels.ExampleWithParametersAndRequestBody import ExampleWithParametersAndRequestBody

class StartServerAndExposeEndpoints:

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(Cryptos, '/api/cryptos')
        self.api.add_resource(CryptosAndPrices, '/api/get-prices')
        self.api.add_resource(ExampleWithParametersAndRequestBody, '/api/example/<string:name>/<int:age>')

        self.app.run(debug=True)


# class PublicEndpoints:

#     def __init__(self):
#         self.start_server()

#         self.expose_resources()

#         self.app.run(debug=True)


#     def create_path_for_endpoint(self, hook):
#         return '/api/' + hook

#     def start_server(self):
#         self.app = Flask(__name__)
#         self.api = Api(self.app)
    
#     def expose_resources(self):
#         self.api.add_resource(Cryptos, self.create_path_for_endpoint('cryptos'))
#         self.api.add_resource(CryptosAndPrices, '/api/get-prices')
#         self.api.add_resource(ExampleWithParametersAndRequestBody, '/api/example/<string:name>/<int:age>')