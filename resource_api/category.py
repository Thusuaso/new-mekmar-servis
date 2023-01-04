from flask import jsonify
from flask_restful import Resource
from views.category import MainPage
class CategoryListApi(Resource):
    def get(self):
        a = MainPage()
        b = a.getMainPageCategory()
        return jsonify(b)