from flask import jsonify
from flask_restful import Resource
from views.fabrication import Fabrication
class FabricationListApi(Resource):
    def get(self):
        a = Fabrication()
        b = a.getFabricationList()
        return jsonify(b)