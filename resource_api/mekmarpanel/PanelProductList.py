from views.mekmarpanel.products import Products
from views.mekmarpanel.kategori import Kategori 
from views.mekmarpanel.finish import Finish
from views.mekmarpanel.ebatlar import Ebatlar
from views.mekmarpanel.fotolar import Fotolar
from views.mekmarpanel.onerilenUrunler import OnerilenUrunler
from flask_restful import Resource
from flask import jsonify,request


class PanelProductListApi(Resource):

    def get(self,kategori):

        product = Products()

        productlist = product.getProductList(kategori)

        return productlist

class PanelKategoriListApi(Resource):

    def get(self):

        kategori = Kategori()
        product = Products()
       

        kategorilist = kategori.getKategoriList()
        productsList = product.getProductList(kategorilist[0]['kategoriadi_en'])
        

        data = {

            "kategorilist" : kategorilist,
            "productslist" : productsList
        }


        return jsonify(data)

class PanelProductDetailApi(Resource):

    def get(self,urunid):

        product = Products()
        finish = Finish()
        ebat = Ebatlar()
        onerilenUrunler = OnerilenUrunler()
        fotolar = Fotolar()

        productdetail = product.getProductDetail(urunid)
        finishlist = finish.getFinishGroupList()
        ebatlist = ebat.getEbatGroupList()
        onerilenUrunList = product.getOnerilenUrunlerList(productdetail['kategori_id'])
        onerilernUrunlerList = onerilenUrunler.getOnerilenUrunList(urunid)
        fotolist = fotolar.getUrunFotoList(urunid)
        renkenlist = product.getEnRenkList() 
        renkfrlist = product.getFrRenkList()
        renkeslist = product.getEsRenkList()

        data = {
            "productdetail" : productdetail,
            "finishlist" : finishlist,
            "ebatlist" : ebatlist,
            "onerilenUrunList" : onerilenUrunList,
            "onerilernUrunlerList" : onerilernUrunlerList,
            "fotolist" : fotolist,
            "renkenlist" : renkenlist,
            'renkfrlist' : renkfrlist,
            "renkeslist" : renkeslist
        }

        return jsonify(data)

class PanelNewProductApi(Resource):

    def get(self):

        product = Products()
        finish = Finish()
        ebat = Ebatlar()
        onerilenUrunler = OnerilenUrunler()
        fotolar = Fotolar()

        productdetail = product.getNewProductModel()
        finishlist = finish.getFinishGroupList()
        ebatlist = ebat.getEbatGroupList()
        onerilenUrunList = product.getNewProductModel()
        onerilernUrunlerList = onerilenUrunler.getNewOnerilenUrunList()
        fotolist = fotolar.getNewFotoList()
        renkenlist = product.getEnRenkList()
        renkfrlist = product.getFrRenkList()
        renkeslist = product.getEsRenkList()
        

        data = {
            "productdetail" : productdetail,
            "finishlist" : finishlist,
            "ebatlist" : ebatlist,
            "onerilenUrunList" : onerilenUrunList,
            "onerilernUrunlerList" : onerilernUrunlerList,
            "fotolist" : fotolist,
            "renkenlist" : renkenlist,
            'renkfrlist' : renkfrlist,
            "renkeslist" : renkeslist
        }

        return jsonify(data)

class PanelProductInsertApi(Resource):

    def post(self):

        data = request.get_json()

        product = Products()

        urunid = product.getNewProductId()
        result = product.veriKaydet(data,urunid)
        print("result - PanelProductInsertApi ",result)
        return jsonify({'status' : result,'urunid' : urunid})

    def put(self):

        data = request.get_json()

        product = Products()

        result = product.veriGuncelle(data)

        return jsonify({'status' : result})
    
class PanelProductDeleteApi(Resource):

    def put(self):

        data = request.get_json()
        print(data)
        product = Products()

        result = product.veriSilme(data['urunid'])

        return jsonify({'status' : result})

class OnerilenUrunIslemApi(Resource):

    def post(self):

        data = request.get_json()

        eklenenler = data['eklenenler']

        silinenler = data['silinenler']

        islem = OnerilenUrunler()

        result = islem.dataKayitIslem(eklenenler,silinenler)

        return jsonify({'status' : result})

class FinishDataIslemApi(Resource):

    def post(self):

        data = request.get_json()

        finish = Finish()
        product = Products()

        result = finish.yuzeyKaydet(data)
        finishlist = product.getFinishUrunList(data['urunid'])

        return jsonify({'status' : result,'finishlist' : finishlist})

    #silme işlemi
    def put(self):
        data = request.get_json()

        finish = Finish()
        product = Products()

        result = finish.yuzeySil(data)
        finishlist = product.getFinishUrunList(data['urunid'])

        return jsonify({'status' : result,'finishlist' : finishlist})

class EbatDataIslemApi(Resource):

    def post(self):

        data = request.get_json()

        ebat = Ebatlar()
        product = Products()

        result = ebat.ebatKaydet(data)

        ebatlist = product.getEbatUrunList(data['urunid'])

        return jsonify({'status' : result,'ebatlist' : ebatlist})

    def put(self):

        data = request.get_json()

        ebat = Ebatlar()
        product = Products()

        result = ebat.ebatGuncelle(data)

        ebatlist = product.getEbatUrunList(data['urunid'])

        return jsonify({'status' : result,'ebatlist' : ebatlist})

class EbatDataIslemSilApi(Resource):

    def put(self):

        data = request.get_json()

        product = Products()

        ebat = Ebatlar()

        result = ebat.ebatSil(data)

        ebatlist = product.getEbatUrunList(data['urunid'])

        return jsonify({'status' : result,'ebatlist' : ebatlist})

class PanelFotoIslemApi(Resource):

    def put(self):

        data = request.get_json()

        fotoSilList = data['fotoSilList']
        fotoSiraDegisim = data['fotoSiraDegisim']

        islem = Fotolar()

        result = islem.fotoSiralaIslem(fotoSilList,fotoSiraDegisim)

        return jsonify({'status' : result})