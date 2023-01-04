from flask import jsonify
from flask_restful import Resource
from views.usa.faq import Faq
class UsaFaqListApi(Resource):
    def get(self):
        a = Faq()
        b = a.getFaqList()
        return jsonify(b)