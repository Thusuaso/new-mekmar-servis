from models.mekmarpanel.cardList import KenarIslemModel,KenarIslemSchema,CardListModel,CardListSchema
from helpers.sqlServer import SqlConnect


class Finish:
    def __init__(self):
        self.data = SqlConnect().data
    
    def getFinishGroupList(self):

        result = self.data.getList(
            """
            select
            finish_en,
			finish_es,
			finish_fr
            from
            MekmarCom_Finish
            group by finish_en , finish_es , finish_fr
            """
        )

        liste = list()
        id = 1

        for item in result:

            model = CardListModel()
            model.id = id 
            model.name = item.finish_en 
            model.name_es = item.finish_es 
            model.name_fr = item.finish_fr 
            liste.append(model)

            id += 1

        schema = CardListSchema(many=True)

        return schema.dump(liste)

    def yuzeyKaydet(self,model):
        try:
            self.data.update_insert(
                """
                insert into MekmarCom_Finish (urunid,finish_en)
                values
                (?,?)
                """,(
                    model['urunid'],model['islemadi']
                )
            ) 

            return True 
        except Exception as e:
            print('Finish Kayıt Hata : ',str(e))
            return False

    def yuzeySil(self,model):

        try:
            self.data.update_insert(
                """
                delete from MekmarCom_Finish where Id=?
                """,(model['id'])
            )
            return True 
        except Exception as e:
            print('Finish Data Sil Hata : ', str(e))
            return False