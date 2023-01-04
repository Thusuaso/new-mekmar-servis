from helpers.sqlServer import SqlConnect
from models.usa.category import *

class Category():
    def __init__(self):
        self.sql = SqlConnect().data
        
    def getMainPageCategoryList(self):
        try:
            categoryList = self.sql.getList("""
                                                    select
                                                    dbo.Get_KategoriAdi(d.UrunKartID) as Kategori,
                                                    count(*) as UrunSayisi
                                                    from
                                                    DepoUrunKartTB d
                                                    where
                                                    d.MekmarSite=1
                                                    group by dbo.Get_KategoriAdi(d.UrunKartID)
                                                    order by count(*) desc
                                                 """)
            liste = list()
            sira = 1
            for item in categoryList:
                model = UsaCategoryListModel()
                model.id = sira
                model.category_en = item.Kategori
                model.category_fr = self.__category_fr(item.Kategori)
                model.category_es = self.__category_es(item.Kategori)
                model.category_produt_count = item.UrunSayisi
                model.category_link = '/usa/usaproducts/' + model.category_en.replace(' ', '-')
                
                sira += 1
                liste.append(model)
                
            schema = UsaCategoryListSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print("getMainPageCategoryList hata",str(e))
            return False
        
    def __category_fr(self,name):
        if(name=='Marble Tiles'):
            return 'Tuiles de Marbre'
        elif (name == 'Travertine Mosaic'):
            return 'Mosaique Travertin'
        elif (name == 'Marble Mosaic'):
            return 'Mosaique Marbre'
        elif (name == 'Travertine Tiles'):
            return 'Tuiles de Travertin'
        elif (name == 'Limestone Tile'):
            return 'Tuiles de Limestone'
        elif (name == 'Glass Mosaic'):
            return 'Mosaique en verre'
        
    def __category_es(self,name):
        if(name=='Marble Tiles'):
            return 'Azulejos de Mármol'
        
        elif (name == 'Travertine Mosaic'):
            return 'Mosaico de Travertino'
        
        elif (name == 'Marble Mosaic'):
            return 'Mosaico de Mármol'
        
        elif (name == 'Travertine Tiles'):
            return 'Azulejos de Travertino'
        
        elif (name == 'Limestone Tile'):
            return 'Azulejo de Piedra Caliza'
        
        elif (name == 'Glass Mosaic'):
            return 'Mosaico de Vidrio'
