from flask_restful import Resource, reqparse

from DataBridge.DataBridge import getCryptosOfInterest, addToCryptosOfInterest

class Cryptos(Resource):

    def get(self):
        contents = getCryptosOfInterest()
        return { "data": contents }, 200

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('new-token', required=True)

        args = parser.parse_args()
        addToCryptosOfInterest(args['new-token'])
        return None, 201