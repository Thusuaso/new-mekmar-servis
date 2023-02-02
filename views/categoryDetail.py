from helpers.sqlServer import SqlConnect
from models.categoryDetail import *
class CategoryDetail:
    def __init__(self):
        self.sql = SqlConnect().data
        
    def getCategoryDetailList(self,category):
        try:
            categoryId = self.sql.getStoreList("""
                                                    select Id  from MekmarCom_Kategoriler where kategori_link=?
                                               
                                               """,(category))[0].Id
            
            categoryDetail = self.sql.getStoreList("""
                                        select 

                                            mp.Id,
                                            mp.urunid,
                                            mp.kategori_id,
                                            mp.urunadi_en,
                                            mp.urunadi_fr,
                                            mp.urunadi_fr,
                                            mp.urunadi_es,
                                            mp.renk_en,
                                            mp.renk_fr,
                                            mp.renk_es,
                                            (select imagePath from MekmarCom_Fotolar mf where mf.urunid = mp.urunid and mf.sira=1) as imagePath,
                                            (select macPath from MekmarCom_Fotolar mf where mf.urunid = mp.urunid and mf.sira=1) as macPath


                                        from MekmarCom_Products mp
                                        where mp.kategori_id=? and yayinla=1
                                      """,(categoryId))
            liste = list()
            for item in categoryDetail:
                model = CategoryDetailModel()
                model.id = item.Id
                model.productId = item.urunid
                model.categoryId = item.kategori_id
                model.productNameEn = item.urunadi_en
                model.productNameFr = item.urunadi_fr
                model.productNameEs = item.urunadi_es
                model.productLink = item.urunadi_en.replace(' ','-')
                model.productColorEn = item.renk_en
                model.productColorFr = item.renk_fr
                model.productColorEs = item.renk_es
                model.webp = item.imagePath
                model.jpeg = item.macPath

                liste.append(model)
                
            schema = CategoryDetailSchema(many=True)
            return schema.dump(liste)

        except Exception as e:
            print('getMainPageCategory hata',str(e))
            return False
        
    def getCategoryDetailFinishList(self,category,finish):
        if(finish == 'All'):
            try:
                
                categoryId = self.sql.getStoreList("""
                                                        select Id  from MekmarCom_Kategoriler where kategori_link=?
                                                
                                                """,(category))[0].Id
                
                categoryDetail = self.sql.getStoreList("""
                                            select 

                                                    mp.Id,
                                                    mp.urunid,
                                                    mp.kategori_id,
                                                    mp.urunadi_en,
                                                    mp.urunadi_fr,
                                                    mp.urunadi_fr,
                                                    mp.urunadi_es,
                                                    mp.renk_en,
                                                    mp.renk_fr,
                                                    mp.renk_es,
                                                    (select imagePath from MekmarCom_Fotolar mf where mf.urunid = mp.urunid and mf.sira=1) as imagePath,
                                                    (select macPath from MekmarCom_Fotolar mf where mf.urunid = mp.urunid and mf.sira=1) as macPath


                                                    from MekmarCom_Products mp
                                                    where mp.kategori_id=? and yayinla=1
                                        """,(categoryId))
                liste = list()
                for item in categoryDetail:
                    model = CategoryDetailModel()
                    model.id = item.Id
                    model.productId = item.urunid
                    model.categoryId = item.kategori_id
                    model.productNameEn = item.urunadi_en
                    model.productNameFr = item.urunadi_fr
                    model.productNameEs = item.urunadi_es
                    model.productLink = item.urunadi_en.replace(' ','-')
                    
                    model.productColorEn = item.renk_en
                    model.productColorFr = item.renk_fr
                    model.productColorEs = item.renk_es
                    model.webp = item.imagePath
                    model.jpeg = item.macPath

                    liste.append(model)
                    
                schema = CategoryDetailSchema(many=True)
                return schema.dump(liste)

            except Exception as e:
                print('getMainPageCategory hata',str(e))
                return False
        else:
            
            try:
                
                categoryId = self.sql.getStoreList("""
                                                        select Id  from MekmarCom_Kategoriler where kategori_link=?
                                                
                                                """,(category))[0].Id
                
                categoryDetail = self.sql.getStoreList("""
                                            select 

                                                    mp.Id,
                                                    mp.urunid,
                                                    mp.kategori_id,
                                                    mp.urunadi_en,
                                                    mp.urunadi_fr,
                                                    mp.urunadi_fr,
                                                    mp.urunadi_es,
                                                    mp.renk_en,
                                                    mp.renk_fr,
                                                    mp.renk_es,
                                                    (select imagePath from MekmarCom_Fotolar mf where mf.urunid = mp.urunid and mf.sira=1) as imagePath,
                                                    (select macPath from MekmarCom_Fotolar mf where mf.urunid = mp.urunid and mf.sira=1) as macPath


                                                    from MekmarCom_Products mp
                                                    inner join MekmarCom_Finish mf on mf.urunid = mp.urunid
                                                    where mp.kategori_id=? and yayinla=1 and mf.finish_en=?
                                        """,(categoryId,finish))
                liste = list()
                for item in categoryDetail:
                    model = CategoryDetailModel()
                    model.id = item.Id
                    model.productId = item.urunid
                    model.categoryId = item.kategori_id
                    model.productNameEn = item.urunadi_en
                    model.productNameFr = item.urunadi_fr
                    model.productNameEs = item.urunadi_es
                    model.productLink = item.urunadi_en.replace(' ','-')
                    
                    model.productColorEn = item.renk_en
                    model.productColorFr = item.renk_fr
                    model.productColorEs = item.renk_es
                    model.webp = item.imagePath
                    model.jpeg = item.macPath

                    liste.append(model)
                    
                schema = CategoryDetailSchema(many=True)
                return schema.dump(liste)

            except Exception as e:
                print('getMainPageCategory hata',str(e))
                return False
        

        