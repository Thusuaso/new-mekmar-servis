from helpers.sqlServer import SqlConnect
from models.mekmarpanel.urunler import UrunlerModel,UrunlerSchema,FotolarModel,FotolarSchema
from models.mekmarpanel.ebatlar import CardListSchema,CardListModel,EbatlarModel,EbatlarSchema


class Products:
    def __init__(self):
        self.data = SqlConnect().data
    
    def getProductList(self,kategori):

        result = self.data.getStoreList(
            """
            select
            p.urunid,
            p.renk_en,
            p.urunkod,
            p.urunadi_en,
            p.tedarikciadi,
            p.sira
            from
            MekmarCom_Products p,MekmarCom_Kategoriler k
            where
            p.kategori_id=k.Id and k.kategoriadi_en=?
            order by p.sira asc
            """,(kategori)
        )

        liste = list()

        fotoList = self.data.getList(
            """
            select * from MekmarCom_Fotolar
            """
        )

        for item in result:

            model = UrunlerModel()
            model.urunid = item.urunid 
            model.urunadi_en = item.urunadi_en 
            model.urunkod = item.urunkod 
            model.tedarikciadi = item.tedarikciadi 
            model.renk_en = item.renk_en
            model.sira = item.sira
            model.fotolar = self.__getFotoList(fotoList,model.urunid)

            liste.append(model)

        schema = UrunlerSchema(many=True)

        return schema.dump(liste)

    def __getFotoList(self,fotolist,urunid):

        liste = list()

        for item in filter(lambda x:x.urunid == urunid,fotolist):
            try:
             
                model = FotolarModel()
                model._id = item.Id
                model.imagePath = item.imagePath 
                model.macPath = item.macPath 
                model.sira = item.sira
                model.nocdn = 'https://mekmar-image.fra1.digitaloceanspaces.com/products/' + item.name + '.' + item.uzanti

                liste.append(model)
            except Exception as e:
                print('Panel getFotoList Hata : ',str(e))

        schema = FotolarSchema(many=True)

        return schema.dump(liste)  

    def getProductDetail(self,urunid):

        item = self.data.getStoreList(
            """
            select
            p.urunid,
            p.urunkod,
            p.urunadi_en,
            p.aciklama_en,
            p.sira,
            p.anahtarlar_en,
            p.birim,
            p.tedarikciadi,
            p.renk_en,
            p.renk_fr,
            p.aciklama_fr,
            p.anahtarlar_fr,
            p.urunadi_fr,
            p.renk_es,
            p.aciklama_es,
            p.anahtarlar_es,
            p.urunadi_es,
            p.yayinla,
            p.testrapor,
            p.kategori_id,
            p.benzerurunlink,
            p.sira,
            p.stonetype
            from
            MekmarCom_Products p
            where 
            p.urunid=?
            """,(urunid)
        )[0]

        model = UrunlerModel()
        model.urunid = item.urunid 
        model.urunadi_en = item.urunadi_en 
        model.aciklama_en = item.aciklama_en 
        model.anahtarlar_en = item.anahtarlar_en 
        model.renk_en = item.renk_en 
        model.urunadi_fr = item.urunadi_fr 
        model.aciklama_fr = item.aciklama_fr 
        model.anahtarlar_fr = item.anahtarlar_fr
        model.renk_es = item.renk_es
        model.urunadi_es = item.urunadi_es
        model.aciklama_es = item.aciklama_es 
        model.anahtarlar_es = item.anahtarlar_es
        model.urunkod = item.urunkod 
        model.birim = item.birim 
        model.benzerUrunLink = item.benzerurunlink 
        model.yayinla = item.yayinla
        model.kategori_id = item.kategori_id
        model.sira = item.sira
        model.kenarIslemList = self.getFinishUrunList(model.urunid)
        model.ebatlar = self.getEbatUrunList(model.urunid)
        model.renk_fr = item.renk_fr
        model.testrapor = item.testrapor
        model.stonetype = item.stonetype
        schema = UrunlerSchema()

        return schema.dump(model)

    def getNewProductModel(self):

        model = UrunlerModel()

        schema = UrunlerSchema()

        return schema.dump(model)

    def getOnerilenUrunlerList(self,kategori_id):

        result = self.data.getStoreList(
            """
            select
            p.urunid,
            p.urunadi_en,
            p.urunadi_fr,
            p.urunadi_es,
            (
            Select 'https://mekmar-image.fra1.digitaloceanspaces.com/products/' +
            f.name + '.' + f.uzanti
            from MekmarCom_Fotolar f where f.urunid=p.urunid and f.sira=1
            ) as foto
            from
            MekmarCom_Products p
            where 
            p.yayinla=1 and p.kategori_id=?
            order by p.sira asc
            """,(kategori_id)
        )

        liste = list()

        for item in result:

            model = UrunlerModel()
            model.urunid = item.urunid 
            model.urunadi_en = item.urunadi_en
            model.urunadi_fr = item.urunadi_fr 
            model.urunadi_es = item.urunadi_es
            model.foto = item.foto
            
            liste.append(model)

        schema = UrunlerSchema(many=True)

        return schema.dump(liste)

    def getEnRenkList(self):

        result = self.data.getList(
            """
            select
            renk_en            
            from
            MekmarCom_Products
            where
            yayinla=1 and renk_en!=''
            and renk_en is not null
            and renk_en!='null'
            group by renk_en
            """
        )  

        liste = list()

        id = 1

        for item in result:

            model = CardListModel()
            model.id = id 
            model.name = item.renk_en             
            liste.append(model)

            id += 1

        schema = CardListSchema(many=True)

        return schema.dump(liste)

    def getFrRenkList(self):

        result = self.data.getList(
            """
           select            
            renk_fr
            from
            MekmarCom_Products
            where
            yayinla=1 and renk_en!=''
            and renk_fr is not null
            and renk_fr!='null'
			and renk_fr!=''
            group by renk_fr
            """
        )  

        liste = list()

        id = 1

        for item in result:

            model = CardListModel()
            model.id = id 
            model.name = item.renk_fr           
            liste.append(model)

            id += 1

        schema = CardListSchema(many=True)

        return schema.dump(liste)

    def getEsRenkList(self):

        result = self.data.getList(
            """
           select            
            renk_es
            from
            MekmarCom_Products
            where
            yayinla=1 and renk_en!=''
            and renk_fr is not null
            and renk_fr!='null'
			and renk_fr!=''
            group by renk_es
            """
        )  

        liste = list()

        id = 1

        for item in result:

            model = CardListModel()
            model.id = id 
            model.name = item.renk_es           
            liste.append(model)

            id += 1

        schema = CardListSchema(many=True)

        return schema.dump(liste)     

    def veriKaydet(self,model,urunid):
        
        try:
            testrapor = ""
            try:
                testrapor = model['testrapor']
            except:
                pass
            self.data.update_insert(
                """
                insert into MekmarCom_Products
                (
                    urunid,
                    kategori_id,
                    urunadi_en,
                    aciklama_en,
                    renk_en,
                    anahtarlar_en,
                    urunadi_fr,
                    aciklama_fr,
                    renk_fr,
                    anahtarlar_fr,
                    urunadi_es,
                    aciklama_es,
                    renk_es,
                    anahtarlar_es,
                    yayinla,
                    tedarikciadi,
                    birim,
                    urunkod,
                    testrapor,
                    sira,
                    stonetype
                )
                values
                (
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,?,?,?,?,?,?,?
                )
                """,
                (
                    urunid,model['kategori_id'],model['urunadi_en'],
                    model['aciklama_en'],model['renk_en'],model['anahtarlar_en'],
                    model['urunadi_fr'],model['aciklama_fr'],model['renk_fr'],
                    model['anahtarlar_fr'],model['urunadi_es'],model['aciklama_es'],model['renk_es'],
                    model['anahtarlar_es'],model['yayinla'],model['tedarikciadi'],
                    model['birim'],model['urunkod'],testrapor,model['sira'],model['stonetype']
                )
            )

            return True 
        except Exception as e:
            print('Product Urun Kayıt Hata : ', str(e))
            return False 

    def veriGuncelle(self,model):

        try:
            self.data.update_insert(
                """
                update MekmarCom_Products set kategori_id=?,urunadi_en=?,
                aciklama_en=?,renk_en=?,anahtarlar_en=?,urunadi_fr=?,
                aciklama_fr=?,renk_fr=?,anahtarlar_fr=?,urunadi_es=?,
                aciklama_es=?,renk_es=?,anahtarlar_es=?,yayinla=?,tedarikciadi=?,
                birim=?,urunkod=?,testrapor=?,sira=?,benzerurunlink=?,stonetype=? where
                urunid=?
                """,
                (
                    model['kategori_id'],model['urunadi_en'],model['aciklama_en'],
                    model['renk_en'],model['anahtarlar_en'],model['urunadi_fr'],
                    model['aciklama_fr'],model['renk_fr'],model['anahtarlar_fr'],
                    model['urunadi_es'],
                    model['aciklama_es'],model['renk_es'],model['anahtarlar_es'],
                    model['yayinla'],model['tedarikciadi'],model['birim'],
                    model['urunkod'],model['testrapor'],model['sira'],model['benzerUrunLink'],model['stonetype'],
                    model['urunid']
                )
            )
            return True 
        except Exception as e:
            print('Product Veri Guncelle Hata : ', str(e))
            return False

    
    def veriSilme(self,urunid):

        try:
            self.data.update_insert(
                """
                
                delete from MekmarCom_Products where urunid=?
                """,
                (
                   urunid
                )
            )
            return True 
        except Exception as e:
            print('Product Veri Guncelle Hata : ', str(e))
            return False

    
    
    
    def getNewProductId(self):

        result = self.data.getList("select max(urunid) as urunid from MekmarCom_Products")[0].urunid

        urunid = result + 1

        return urunid

    def getFinishUrunList(self,urunid):
        result = self.data.getStoreList(
            """
            select * from MekmarCom_Finish
            where urunid=?
            """,(urunid)
        )

        liste = list()

        for item in result:
            model = CardListModel()
            model.id = item.Id 
            model.name = item.finish_en
            model.name_es = item.finish_es
            model.name_fr = item.finish_fr

            liste.append(model)

        schema = CardListSchema(many=True)

        return schema.dump(liste)

    def getEbatUrunList(self,urunid):

        result = self.data.getStoreList(
            """
            select * from MekmarCom_Ebatlar
            where urunid=?
            """,(urunid)
        )

        liste = list()

        for item in result:

            model = EbatlarModel()
            model.id = item.Id 
            model.urunid = item.urunid 
            model.ebat = item.ebat 
            model.fiyat= float(item.fiyat)

            liste.append(model)

        schema = EbatlarSchema(many=True)

        return schema.dump(liste)
