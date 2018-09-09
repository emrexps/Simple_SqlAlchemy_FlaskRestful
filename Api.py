
from Model import *
from Operations import (insert,getById,listAll)
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('surname')

class Insert(Resource):
    def put(self, name,surname):
        insert(name,surname)
        return "success", 201

"""post method usage..."""
class Add(Resource):
    def post(self):
        args = parser.parse_args()
        insert(args['name'],args['surname'])
        return "added sucess",200


class ReadSpecific(Resource):
    def get(self,id):
        return getById(id)

class ReadAll(Resource):
    def get(self):
        return listAll()



api.add_resource(Insert, '/insert/<name>/<surname>')
api.add_resource(ReadSpecific,'/getbyid/<id>')
api.add_resource(ReadAll,'/getall')
api.add_resource(Add,'/add')



if __name__ == '__main__':
    app.run(debug=True)
