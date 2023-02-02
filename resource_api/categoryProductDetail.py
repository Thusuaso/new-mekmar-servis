from flask import jsonify
from flask_restful import Resource
from views.categoryProductDetail import *
class CategoryProductDetailApi(Resource):
    def get(self,productName):
        a = CategoryProductDetail()
        b = a.getCategoryProductDetail(productName.replace('-',' '))
        c = a.getCategoryProductPhotos(productName.replace('-',' '))
        d = a.getCategoryProductDimension(productName.replace('-',' '))
        e = a.getCategoryProductSuggested(productName.replace('-',' '))
        data = {
            'productDetail':b,
            'productPhotos':c,
            'productDimension':d,
            'productSuggested':e
        }
        return jsonify(data)
    
