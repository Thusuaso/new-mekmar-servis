from flask import jsonify
from flask_restful import Resource
from views.categoryColorList import *
class CategoryDetailColorListApi(Resource):
    def get(self,category):
        a = CategoryDetailColorList()
        b = a.getCategoryDetailColorList(category)
        c = a.getCategoryDetailFinishList(category)
        data = {
            'colorList':b,
            'finishList':c
        }
        return jsonify(data)