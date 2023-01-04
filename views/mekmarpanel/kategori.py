from models import KategoriModel,KategoriSchema
from helpers.sqlServer import SqlConnect


class Kategori:
    def __init__(self):
        self.data = SqlConnect().data

    def getKategoriList(self):

        result = self.data.getList(
            """
            select * from MekmarCom_Kategoriler
            order by sira asc
            """
        )

        liste = list()

        for item in result:

            model = KategoriModel()
            model.kategori_id = item.Id 
            model.kategoriadi_en = item.kategoriadi_en 
            model.kategoriadi_fr = item.kategoriadi_fr 
            model.kategoriadi_es = item.kategoriadi_es

            liste.append(model)

        schema = KategoriSchema(many=True)

        return schema.dump(liste)


