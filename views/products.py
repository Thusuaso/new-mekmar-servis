from helpers.sqlServer import SqlConnect
from models.products import *
class Products:
    def __init__(self):
        self.sql = SqlConnect().data
        
    def getProductsList(self):
        try:
            productsList = self.sql.getList("""
                                                select 
                                                Id,
                                                kategoriadi_en,
                                                kategoriadi_fr,
                                                kategoriadi_es 
                                                from MekmarCom_Kategoriler
                                            
                                            """)
            liste = list()
            for item in productsList:
                model = ProductsListModel()
                model.id = item.Id
                model.category_en = item.kategoriadi_en
                model.category_fr = item.kategoriadi_fr
                model.category_es = item.kategoriadi_es
                liste.append(model)
            schema = ProductsListSchema(many=True)
            return schema.dump(liste)
                
        
        except Exception as e:
            print("getProductsList hata",str(e))
            return False