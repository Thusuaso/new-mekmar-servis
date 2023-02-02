from flask import Flask
from flask_restful import Api,Resource
from flask_cors import CORS
from resource_api.category import *
from resource_api.products import *
from resource_api.slider import *
from resource_api.fabrication import *
from resource_api.videos import *
from resource_api.sendmail import *
from resource_api.login import *
from resource_api.register import *
from resource_api.galleria import *



from resource_api.categoryDetail import *
from resource_api.categoryColorList import *
from resource_api.categoryProductDetail import *
from resource_api.categoryProductDetail import *
from resource_api.mekmarpanel.PanelProductList import *
from resource_api.usa.productList import *

from resource_api.usa.category import *
from resource_api.usa.filters import *
from resource_api.usa.faq import *







app = Flask(__name__)
CORS(app)

api = Api(app)

api.add_resource(CategoryListApi,"/home/categoryList",methods=["GET"])
api.add_resource(ProductsListApi,"/home/productList",methods=["GET"])
api.add_resource(SlideListApi,"/home/slideList",methods=["GET"])
api.add_resource(FabricationListApi,"/home/fabricationList",methods=["GET"])
api.add_resource(VideosListApi,"/home/videosList",methods=["GET"])
api.add_resource(SendMailApi,"/home/sendMail",methods=['POST'])
api.add_resource(CategoryDetailListApi,"/home/categoryDetail/<string:category>",methods=['GET'])
api.add_resource(CategoryDetailColorListApi,"/home/categoryDetailColor/<string:category>",methods=['GET'])
api.add_resource(CategoryProductDetailApi,'/home/categoryProductDetail/<string:productName>',methods=['GET'])
api.add_resource(CategoryDetailByFinishListApi,'/home/categoryProductFinish/<string:category>/<string:finish>')
api.add_resource(LoginApi,'/home/login/<string:username>',methods=['GET'])
api.add_resource(RegisterApi,'/home/register',methods=['POST'])
api.add_resource(GalleriaPhotosApi,'/mekmar/galleria/getPhotos',methods=['GET'])

#Depo
api.add_resource(UsaCategoryListApi,"/usa/home/categoryProductList",methods=['GET'])
api.add_resource(UsaProductListApi,"/usa/home/usaProductList",methods=['GET'])
api.add_resource(UsaUsageOfAreaProductListApi,'/usa/home/usageOfAreProductList/<string:name>',methods=['GET'])
api.add_resource(UsaColorProductListApi,"/usa/home/colorProductList/<string:name>",methods=['GET'])
api.add_resource(UsaSizeProductListApi,"/usa/home/sizeProductList/<string:name>",methods=['GET'])
api.add_resource(UsaCategoryProductListApi,'/usa/home/categoryProductList/<string:name>',methods=['GET'])
api.add_resource(UsaFaqListApi,'/usa/home/faqList',methods=['GET'])
api.add_resource(UsaProductDetailListApi,'/usa/home/productDetailList/<int:id>',methods=['GET'])



#Mekmar Panel İşlemleri
api.add_resource(PanelProductListApi,'/panelProductList/productKategoriList/<string:kategori>',methods=['GET'])
api.add_resource(PanelKategoriListApi,'/panel/mekmarcom/kategoriList',methods=['GET'])
api.add_resource(PanelProductDetailApi,'/panel/mekmarcom/productDetail/<int:urunid>',methods=['GET'])
api.add_resource(PanelProductInsertApi,'/panel/mekmarcom/productDetail/VeriKayıt',methods=['POST','GET','PUT'])
api.add_resource(PanelProductDeleteApi,'/panel/mekmarcom/productDetail/urunSil',methods=['POST','GET','PUT'])
api.add_resource(PanelNewProductApi,'/panel/mekmarcom/productDetail/newProduct',methods=['GET'])
api.add_resource(OnerilenUrunIslemApi,'/panel/mekmarcom/productDetail/onerilenUrunKayit',methods=['GET','POST'])
api.add_resource(FinishDataIslemApi,'/panel/mekmarcom/productDetail/finishDataIslem',methods=['GET','POST','PUT'])
api.add_resource(EbatDataIslemApi,'/panel/mekmarcom/productDetail/ebatDataIslem',methods=['GET','POST','PUT'])
api.add_resource(EbatDataIslemSilApi,'/panel/mekmarcom/productDetail/ebatDataSil',methods=['GET','PUT'])
api.add_resource(PanelFotoIslemApi,'/panel/mekmarcom/fotolar/SiraKayitDegisim',methods=['PUT','GET'])



if __name__ == '__main__':
    app.run(port=5000,debug=True)
