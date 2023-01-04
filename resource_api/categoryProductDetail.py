from flask import jsonify
from flask_restful import Resource
from views.categoryProductDetail import *
class CategoryProductDetailApi(Resource):
    def get(self,productName):
        a = CategoryProductDetail()
        b = a.getCategoryProductDetail(productName)
        c = a.getCategoryProductPhotos(productName)
        d = a.getCategoryProductDimension(productName)
        e = a.getCategoryProductSuggested(productName)
        data = {
            'productDetail':b,
            'productPhotos':c,
            'productDimension':d,
            'productSuggested':e
        }
        return jsonify(data)
    
