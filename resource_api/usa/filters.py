from flask import jsonify
from flask_restful import Resource
from views.usa.filters import Filters
from views.usa.productList import Products


class UsaUsageOfAreaProductListApi(Resource):
    def get(self,name):
        a = Filters()
        b = Products()
        productList = a.getUsageOfAreaProductList(name)
        outOfStockList = b.getProductOutofStockList()
        usageList = b.getUsageAreasList()
        colorList = b.getColorList()
        sizeList = b.getSizeList()

        data = {
            'productList':productList,
            'usageList':usageList,
            'colorList':colorList,
            'sizeList':sizeList,
            'outOfStockList':outOfStockList

        }
        return jsonify(data)
    
class UsaColorProductListApi(Resource):
    def get(self,name):
        a = Filters()
        b = Products()
        productList = a.getColorProductList(name)
        outOfStockList = b.getProductOutofStockList()
        usageList = b.getUsageAreasList()
        colorList = b.getColorList()
        sizeList = b.getSizeList()

        data = {
            'productList':productList,
            'usageList':usageList,
            'colorList':colorList,
            'sizeList':sizeList,
            'outOfStockList':outOfStockList

        }
        return jsonify(data)
    
    
class UsaSizeProductListApi(Resource):
    def get(self,name):
        a = Filters()
        b = Products()
        productList = a.getSizeProductList(name)
        outOfStockList = b.getProductOutofStockList()
        usageList = b.getUsageAreasList()
        colorList = b.getColorList()
        sizeList = b.getSizeList()

        data = {
            'productList':productList,
            'usageList':usageList,
            'colorList':colorList,
            'sizeList':sizeList,
            'outOfStockList':outOfStockList

        }
        return jsonify(data)