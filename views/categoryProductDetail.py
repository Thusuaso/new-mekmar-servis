from helpers.sqlServer import SqlConnect
from models.categoryProductDetail import *
class CategoryProductDetail:
    def __init__(self):
        self.sql = SqlConnect().data
        
    def getCategoryProductDetail(self,productName):
        try:
            id = self.sql.getStoreList("""
                                            select Id from MekmarCom_Products where urunadi_en=?

                                       
                                       """,(productName))[0].Id            
            products = self.sql.getStoreList("""
                                                select 
                                                        *

                                                    from MekmarCom_Products mp

                                                    where mp.Id=?
                                            
                                            """,(id))[0]
            liste = list()
            model = CategoryProductDetailModel()
            model.product_name_en = products.urunadi_en
            model.product_name_fr = products.urunadi_fr
            model.product_name_es = products.urunadi_es
            model.product_description_en = products.aciklama_en
            model.product_description_fr = products.aciklama_fr
            model.product_description_es = products.aciklama_es
            model.product_color_en = products.renk_en
            model.product_color_fr = products.renk_fr
            model.product_color_es = products.renk_es
            model.product_test_rapor = products.testrapor
            model.product_code = products.urunkod
            model.product_queue = products.sira
            model.product_unit = products.birim
            model.product_stoneType = products.stonetype
            

            liste.append(model)
            schema = CategoryProductDetailSchema(many=True)
            return schema.dump(liste)
                
        
        except Exception as e:
            print("getProductsList hata",str(e))
            return False
        
    def getCategoryProductPhotos(self,productName):
        try:
            id = self.sql.getStoreList("""
                                            select Id from MekmarCom_Products where urunadi_en=?

                                       
                                       """,(productName))[0].Id
            urunId = self.sql.getStoreList("""

                                            select urunid from MekmarCom_Products where Id=?
                                           
                                           """,(id))[0].urunid
            
            photos = self.sql.getStoreList("""
                                            select * from MekmarCom_Fotolar where urunid=?
                                           
                                           """,(urunId))
            liste = list()
            index = 0
            for item in photos:
                model = CategoryProductDetailPhotosModel()
                model.index = index
                model.id = item.Id 
                model.product_id = item.urunid
                model.product_photos_name = item.name
                model.product_webp = item.imagePath
                model.product_jpeg = item.macPath
                model.product_queue = item.sira
                index += 1
                liste.append(model)
            schema = CategoryProductDetailPhotosSchema(many=True)
            return schema.dump(liste)          
        except Exception as a:
            print("getCategoryProductPhotos hata",str(a))
            return False
        
    def getCategoryProductDimension(self,productName):
        try:
            id = self.sql.getStoreList("""
                                            select Id from MekmarCom_Products where urunadi_en=?

                                       
                                       """,(productName))[0].Id
            urunId = self.sql.getStoreList("""

                                            select urunid from MekmarCom_Products where Id=?
                                           
                                           """,(id))[0].urunid
            
            dimensions = self.sql.getStoreList("""
                                            select * from MekmarCom_Ebatlar where urunid=?
                                           
                                           """,(urunId))
            liste = list()
            for item in dimensions:
                model = CategoryProductDetailEbatsModel()
                model.id = item.Id 
                model.product_id = item.urunid
                model.product_dimension = item.ebat
                model.product_unit = item.birim
                model.product_price = item.fiyat
                liste.append(model)
            schema = CategoryProductDetailEbatsSchema(many=True)
            return schema.dump(liste)
            
        except Exception as a:
            print("getCategoryProductEbats hata",str(a))
            return False
        
    def getCategoryProductSuggested(self,productName):
        try:
            id = self.sql.getStoreList("""
                                            select Id from MekmarCom_Products where urunadi_en=?

                                       
                                       """,(productName))[0].Id
            urunId = self.sql.getStoreList("""

                                            select urunid from MekmarCom_Products where Id=?
                                           
                                           """,(id))[0].urunid
            
            suggested = self.sql.getStoreList("""
                                            select * from MekmarCom_OnerilenUrunler where urunid=?                                           
                                           """,(urunId))
            liste = list()
            for item in suggested:
                result = self.sql.getStoreList("""
                                        select 

                                            (select mf.imagePath from MekmarCom_Fotolar mf where mf.urunid = mp.urunid and mf.sira=1) as Webp,
                                            (select mf.macPath from MekmarCom_Fotolar mf where mf.urunid = mp.urunid and mf.sira=1) as Jpeg,
                                            mp.urunadi_en,
                                            mp.urunadi_fr,
                                            mp.urunadi_es,
                                            mp.Id,
                                            mp.urunid,
                                            (select mk.kategoriadi_en from MekmarCom_Kategoriler mk where mk.Id = mp.kategori_id) as category_name


                                        from MekmarCom_Products mp where mp.urunid=?
                                      
                                      """,(item.onerilenurunid))[0]
                model = CategoryProductDetailSuggestedModel()
                model.id = result.Id 
                model.product_id = result.urunid
                model.product_name_en  = result.urunadi_en
                model.product_name_fr = result.urunadi_fr
                model.product_name_es = result.urunadi_es
                model.product_webp = result.Webp
                model.product_jpeg = result.Jpeg
                model.product_category_name = result.category_name
                
                liste.append(model)
            schema = CategoryProductDetailSuggestedSchema(many=True)
            return schema.dump(liste)
            
        except Exception as a:
            print("getCategoryProductSuggested hata",str(a))
            return False
        