from flask import jsonify
from flask_restful import Resource
from views.products import Products
class ProductsListApi(Resource):
    def get(self):
        a = Products()
        b = a.getProductsList()
        return jsonify(b)
    