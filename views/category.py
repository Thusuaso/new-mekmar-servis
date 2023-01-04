from helpers.sqlServer import SqlConnect
from models.category import MainPageCategorySchema,MainPageCategoryModel
class MainPage:
    def __init__(self):
        self.sql = SqlConnect().data
        
    def getMainPageCategory(self):
        try:
            
            category = self.sql.getList("""
                                        select * from MekmarCom_Kategoriler
                                      """)
            liste = list()
            for item in category:
                model = MainPageCategoryModel()
                model.category_id = item.Id
                model.category_en = item.kategoriadi_en
                model.category_fr = item.kategoriadi_fr
                model.category_es = item.kategoriadi_es
                model.category_link = item.kategori_link
                model.category_foto_en = 'https://mekmar-image.fra1.digitaloceanspaces.com/menu/en/' + item.foto_en
                model.category_foto_fr = 'https://mekmar-image.fra1.digitaloceanspaces.com/menu/fr/' + item.foto_fr
                model.category_foto_es = 'https://mekmar-image.fra1.digitaloceanspaces.com/menu/es/' +item.foto_es
                model.category_sira = item.sira
                liste.append(model)
                
            schema = MainPageCategorySchema(many=True)
            return schema.dump(liste)
                
            
            
            
            
        except Exception as e:
            print('getMainPageCategory hata',str(e))
            return False