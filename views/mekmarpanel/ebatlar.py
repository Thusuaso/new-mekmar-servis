from models import CardListSchema,CardListModel 
from helpers.sqlServer import SqlConnect


class Ebatlar:
    def __init__(self):
        self.data = SqlConnect().data 

    def getEbatGroupList(self):

        result = self.data.getList(
            """
            Select ebat from MekmarCom_Ebatlar group by ebat
            """
        )

        liste = list()

        id = 1

        for item in result:

            model = CardListModel()
            model.id = id 
            model.name = item.ebat 

            liste.append(model)

            id += 1

        schema = CardListSchema(many=True)

        return schema.dump(liste)


    def ebatKaydet(self,model):
        try:
            result = self.data.update_insert(
                """
                insert into MekmarCom_Ebatlar (urunid,ebat,fiyat)
                values
                (?,?,?)
                """,
                (model['urunid'],model['ebat'],model['fiyat'])
            )

            return True 

        except Exception as e:
            print('Ebat Data Kayıt Hata : ',str(e))
            return False

    def ebatGuncelle(self,model):

        try:
            result = self.data.update_insert(
                """
                update MekmarCom_Ebatlar set ebat=?,fiyat=? where 
                Id=?
                """,
                (model['ebat'],model['fiyat'],model['id'])
            )

            return True 
        except Exception as e:
            print('Ebat Data Guncelle Hata :',str(e))
            return False 
    
    def ebatSil(self,model):

        try:
            self.data.update_insert(
                """
                delete from MekmarCom_Ebatlar where Id=?
                """,(model['id'])
            )

            return True 
        except Exception as e:
            print("Ebat Data Sil Hata : ",str(e))
            return False