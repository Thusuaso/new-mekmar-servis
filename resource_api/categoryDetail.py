from flask import jsonify
from flask_restful import Resource
from views.categoryDetail import *
class CategoryDetailListApi(Resource):
    def get(self,category):
        a = CategoryDetail()
        b = a.getCategoryDetailList(category)
        return jsonify(b)
    
class CategoryDetailListAllApi(Resource):
    def get(self):
        a = CategoryDetail()
        b = a.getCategoryDetailListAll()
        return jsonify(b)
    
    
class CategoryDetailByFinishListApi(Resource):
    def get(self,category,finish):
        a = CategoryDetail()
        b = a.getCategoryDetailFinishList(category,finish)
        return jsonify(b)