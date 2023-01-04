from flask import jsonify
from flask_restful import Resource
from views.sendmail import SendMail
class SendMailApi(Resource):
    def post(self):
        a = SendMail()
        b = a.send()
        return jsonify(b)