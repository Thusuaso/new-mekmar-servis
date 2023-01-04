from flask import jsonify
from flask_restful import Resource
from views.usa.category import Category
class UsaCategoryListApi(Resource):
    def get(self):
        a = Category()
        b = a.getMainPageCategoryList()
        return jsonify(b)