from flask_restful import Resource, reqparse, request


class ExampleWithParametersAndRequestBody(Resource):
    
    def get(self, name, age):
        package = {
            "data": {
                "name": name,
                "age": age
            }
        }
        return package

    def put(self, name, age):
        # the string 'key' comes from postman in the form-data in the body section
        return request.form['key'], 201