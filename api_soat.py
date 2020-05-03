from flask import Flask
from flask_restful import Resource, Api
#from flask_cors import CORS
import soat_tools as tt


app = Flask(__name__)
#CORS(app)
api = Api(app)

class Hello(Resource):
    def get(self, name):
        return {"Hello":name}

class Cotizar(Resource):
    def get(self, placa):
    	respuesta=tt.getFinalPrice(placa)
    	return respuesta



api.add_resource(Cotizar, '/cotizar/<placa>')
api.add_resource(Hello, '/hello/<name>')


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port="5000")