from flask import jsonify
from flask_restful import Resource
from views.login import Login
class LoginApi(Resource):
    def get(self,username):
        a = Login()
        b = a.getLogin(username)
        return jsonify({'status':b})