
from Model import *
from Operations import (insert,getById,listAll)
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class Insert(Resource):
    def put(self, name,surname):
        insert(name,surname)
        return "success", 201

class ReadSpecific(Resource):
    def get(self,id):
        return getById(id)

class ReadAll(Resource):
    def get(self):
        return listAll()



api.add_resource(Insert, '/insert/<name>/<surname>')
api.add_resource(ReadSpecific,'/getbyid/<id>')
api.add_resource(ReadAll,'/getall')




if __name__ == '__main__':
    app.run(debug=True)
