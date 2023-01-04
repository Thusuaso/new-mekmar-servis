from models import FotolarModel,FotolarSchema
from helpers.sqlServer import SqlConnect


class Fotolar:
    def __init__(self):
        self.data = SqlConnect().data
        self.url = 'https://mekmar-image.fra1.digitaloceanspaces.com/products/'

    def getUrunFotoList(self,urunid):

        result = self.data.getStoreList(
            """
            select
            'https://mekmar-image.fra1.digitaloceanspaces.com/products/'
            + name + '.' + uzanti as foto,
            Id,
            sira,
            name + '.' + uzanti as name
            from
            MekmarCom_Fotolar
            where 
            urunid=?
            order by sira asc
            """,(urunid)
        )

        liste = list()

        for item in result:

            model = FotolarModel()
            model.id = item.Id 
            model.nocdn = item.foto
            model.sira = item.sira
            model.name = item.name 

            liste.append(model)

        schema = FotolarSchema(many=True)

        return schema.dump(liste)

    def getNewFotoList(self):

        model = FotolarModel()

        schema = FotolarSchema()

        return schema.dump(model)

    def fotoKayit(self,file):
        try:
            name = str(file).split('.')[0]
            uzanti = str(file).split('.')[1]
            urunid = int(name.split('-')[1])
            sira = int(name.split('-')[2])

            imagePath = self.url + name + '.webp' 
            macPath =  self.url + name + '.' + uzanti

            kontrol = self.__fotoKontrol(urunid,sira)
            if uzanti != 'webp':
                if kontrol > 0:
                    self.__fotoGuncelle(name,uzanti,urunid,sira,imagePath,macPath)
                else:
                    self.__fotoKayit(name,uzanti,urunid,sira,imagePath,macPath)
            
            return True 
        except Exception as e:
            print('Fotolar fotokayıt Hata : ',str(e))
            return False
   
    def __fotoKontrol(self,urunid,sira):

        result = self.data.getStoreList(
            """
            select count(*) as durum from MekmarCom_Fotolar where
            urunid=? and sira=?
            """,(urunid,sira)
        )[0].durum

        return result

    def __fotoGuncelle(self,name,uzanti,urunid,sira,imagePath,macPath):
        self.data.update_insert(
                """
                update MekmarCom_Fotolar set name=?,
                uzanti=?,imagePath=?,
                macPath=? where urunid=? and sira=?
                """,
                (
                   name,uzanti,imagePath,macPath,urunid,sira
                )
        )

    def __fotoKayit(self,name,uzanti,urunid,sira,imagePath,macPath):

        self.data.update_insert(
            """
            insert into MekmarCom_Fotolar (urunid,name,uzanti,imagePath,macPath,sira)
            values
            (?,?,?,?,?,?)
            """,
            (
                urunid,name,uzanti,imagePath,macPath,sira
            )
        )

    def fotoSiralaIslem(self,fotoSilList,fotoSiraDegisim):
        try:
            for item in fotoSilList:
              
                self.__fotoSil(item['id'])

            for item in fotoSiraDegisim:
                self.__fotoSiraDegistir(item['id'],item['sira'])
            return True 
        except Exception as e:
            print("Fotolar Foto Sıra Değiştir Hata : ",str(e))
            return False

    def __fotoSiraDegistir(self,id,sira):

        self.data.update_insert(
            """
            update MekmarCom_Fotolar set sira=? where Id=?
            """,(sira,id)
        )

    def __fotoSil(self,id):
        print('Foto Sil : ', id)
        self.data.update_insert(
            """
            delete from MekmarCom_Fotolar where Id=?
            """,(id)
        )


