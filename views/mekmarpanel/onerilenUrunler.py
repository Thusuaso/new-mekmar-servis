from models.mekmarpanel.onerilenUrunler import OnerilenUrunlerModel,OnerilenUrunlerSchema
from helpers.sqlServer import SqlConnect


class OnerilenUrunler:
    def __init__(self):
        self.data = SqlConnect().data

    def getOnerilenUrunList(self,urunid):

        result = self.data.getStoreList(
            """
            select
            o.onerilenurunid,
            (select k.urunadi_en from MekmarCom_Products k where k.urunid=o.onerilenurunid) as urunadi_en,
            (select k.urunadi_fr from MekmarCom_Products k where k.urunid=o.onerilenurunid) as urunadi_fr,
			(select k.urunadi_fr from MekmarCom_Products k where k.urunid=o.onerilenurunid) as urunadi_es,
            (Select 'https://mekmar-image.fra1.digitaloceanspaces.com/products/' + f.name + '.' + 
            f.uzanti from MekmarCom_Fotolar f where f.urunid=o.onerilenurunid and f.sira=1) as foto
            from
            MekmarCom_OnerilenUrunler o
            where
            o.urunid in
            (
            Select p.urunid from MekmarCom_Products p where
            p.urunid=o.urunid and p.urunid=?
            )
            """,(urunid)
        )

        liste = list()

        for item in result:
            
            model = OnerilenUrunlerModel()
            model.onerilenurunid = item.onerilenurunid
            model.benzerurunid = model.onerilenurunid
            model.urunadi_en = item.urunadi_en 
            model.urunadi_fr = item.urunadi_fr 
            model.urunadi_es = item.urunadi_es
            model.nocdn = item.foto 

            liste.append(model)

        schema = OnerilenUrunlerSchema(many=True)

        return schema.dump(liste)

    def getNewOnerilenUrunList(self):

        model = OnerilenUrunlerModel()

        schema = OnerilenUrunlerSchema()

        return schema.dump(model)

    def dataKayitIslem(self,eklenenler,silineler):

        try:

            for item in eklenenler:
                self.__dataKayit(item['urunid'],item['benzerurunid'])

            for item in silineler:
                print('Item : ',item)
                self.__dataSil(item['urunid'],item['onerilenurunid'])
        
            return True 
        except Exception as e:
            print('Onerilen Urunler Data Kayıt Hata : ', str(e))
            return False

    def __dataKayit(self,urunid,onerilenurunid):

        self.data.update_insert(
            """
            insert into MekmarCom_OnerilenUrunler (urunid,onerilenurunid)
            values
            (?,?)
            """,(urunid,onerilenurunid)
        )
    
    def __dataSil(self,urunid,onerilenurunid):
        print('UrunId : ',urunid)
        print('onerilenurunid : ',onerilenurunid)
        self.data.update_insert(
            """
            delete from MekmarCom_OnerilenUrunler where urunid=? and onerilenurunid=?
            """,(urunid,onerilenurunid)
        )

