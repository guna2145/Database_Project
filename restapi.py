from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class Restapi(Resource):

    ## Function for the GET Request - READ Operation ##
    def get(self):
        return {'data':'logan'}

    ## Function for the POST Request - CREATE Operations ##
    def post(self):
        pass

    ## Function for the PUT Request -  UPDATE Operations ##
    def put(self):
        pass

    ## Function for the DELETE Request - DELETE Operations ##
    def delete(self):
        pass

## Instantiate the Api resource
api.add_resource(Restapi,'/')

if __name__ == "__main__":
    app.run()