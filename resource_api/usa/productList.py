from flask import jsonify
from flask_restful import Resource
from views.usa.productList import Products
class UsaProductListApi(Resource):
    def get(self):
        a = Products()
        productList = a.getProductList()
        outOfStockList = a.getProductOutofStockList()
        usageList = a.getUsageAreasList()
        colorList = a.getColorList()
        sizeList = a.getSizeList()

        data = {
            'productList':productList,
            'outOfStockList':outOfStockList,
            'usageList':usageList,
            'colorList':colorList,
            'sizeList':sizeList

        }
        return jsonify(data)
    
class UsaCategoryProductListApi(Resource):
    def get(self,name):
        a = Products()
        productList = a.getCategoryProductList(name)
        outOfStockList = a.getProductOutofStockList()
        usageList = a.getUsageAreasList()
        colorList = a.getColorList()
        sizeList = a.getSizeList()

        data = {
            'productList':productList,
            'outOfStockList':outOfStockList,
            'usageList':usageList,
            'colorList':colorList,
            'sizeList':sizeList

        }
        return jsonify(data)
    
    
class UsaProductDetailListApi(Resource):
    def get(self,id):
        a = Products()
        productDetailList = a.getProductDetailList(id)
        return jsonify(productDetailList)
    
    

        