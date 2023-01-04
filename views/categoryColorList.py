from helpers.sqlServer import SqlConnect
from models.categoryColorList import *
class CategoryDetailColorList:
    def __init__(self):
        self.sql = SqlConnect().data
        
    def getCategoryDetailColorList(self,category):
        try:
            categoryId = self.sql.getStoreList("""
                                                    select Id  from MekmarCom_Kategoriler where kategoriadi_en=?
                                               
                                               """,(category))[0]
            categoryDetail = self.sql.getStoreList("""
                                        select 
                                            mp.renk_en,
                                            mp.renk_fr,
                                            mp.renk_es,
                                            count(mp.renk_en) as enCount,
                                            count(mp.renk_fr) as frCount,
                                            count(mp.renk_es) as esCount
                                        from MekmarCom_Products mp
                                        where mp.kategori_id=? and yayinla=1

                                        group by mp.renk_en,mp.renk_fr,mp.renk_es
                                      """,(categoryId))
            liste = list()
            color_sum = 0
            for item in categoryDetail:
                model = CategoryDetailColorModel()
                model.color_en = item.renk_en
                model.color_fr = item.renk_fr
                model.color_es = item.renk_es
                model.color_en_count = item.enCount
                model.color_fr_count = item.frCount
                model.color_es_count = item.esCount
                color_sum += item.enCount
            
                liste.append(model)
            
            schema = CategoryDetailColorSchema(many=True)
            return schema.dump(liste)

            
        except Exception as e:
            print('getMainPageCategory hata',str(e))
            return False
        

    def getCategoryDetailFinishList(self,category):
        try:
            categoryId = self.sql.getStoreList("""
                                                    select Id  from MekmarCom_Kategoriler where kategoriadi_en=?
                                               
                                               """,(category))[0]
            categoryDetail = self.sql.getStoreList("""
                                        select 

                                            count(mf.finish_en) count,
                                            mf.finish_en,
                                            mf.finish_fr,
                                            mf.finish_es

                                        from 
                                        MekmarCom_Products mp
                                        inner join MekmarCom_Finish mf on mf.urunid = mp.urunid


                                        where mp.kategori_id=?
                                        group by mf.finish_en,mf.finish_es,mf.finish_fr
                                      """,(categoryId))
            liste = list()
            for item in categoryDetail:
                model = CategoryDetailFinishModel()
                model.finish_en =item.finish_en
                model.finish_fr =item.finish_fr
                model.finish_es =item.finish_es
                model.finish_count = item.count
                
                liste.append(model)
            
            schema = CategoryDetailFinishSchema(many=True)
            return schema.dump(liste)

            
        except Exception as e:
            print('getMainPageCategory hata',str(e))
            return False
        