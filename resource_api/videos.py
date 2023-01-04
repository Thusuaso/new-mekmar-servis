from flask import jsonify
from flask_restful import Resource
from views.videos import Videos
class VideosListApi(Resource):
    def get(self):
        a = Videos()
        b = a.getVideosList()
        return jsonify(b)