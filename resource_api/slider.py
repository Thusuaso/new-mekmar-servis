from flask import jsonify
from flask_restful import Resource
from views.slider import Slider

class SlideListApi(Resource):
    def get(self):
        a = Slider()
        b = a.getSliderOneList()
        c = a.getSliderTwoList()
        d = a.getSliderThreeList()
        e = a.getSliderFourList()
        data = {
            'slideOne':b,
            'slideTwo':c,
            'slideThree':d,
            'slideFour':e
        }
        return jsonify(data)