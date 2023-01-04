from flask import jsonify,request
from flask_restful import Resource
from views.register import Register
class RegisterApi(Resource):
    def post(self):
        data = request.get_json()
        a = Register()
        b = a.setRegister(data)
        return jsonify({'status':b})