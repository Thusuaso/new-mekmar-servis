from helpers.sqlServer import SqlConnect
from models.usa.productList import *
from models.usa.card import *
from models.usa.photos import *

class Products():
    def __init__(self):
        self.sql = SqlConnect().data
        self.fotolar = self.sql.getList(
            """
            Select * from DepoUrunKart_MekmarFotolarTB
            """
        )
        
        
    def getProductList(self):
        try:
            products = self.sql.getList("""
                                            Select
                                            k.ID,
                                            u.Fiyat,
                                            u.MaxStock,
                                            dbo.get_YeniDepoStok(k.ID,k.Devir) * k.KutuSqft as Stok_Sqft,
                                            u.Size,
                                            u.Sira,
                                            u.urunadi_en,
                                            u.aciklama_en,
                                            u.urunadi_fr,
                                            u.aciklama_fr,
                                            u.urunadi_es,
                                            u.aciklama_es,
                                            (select dmf.Webp from DepoUrunKart_MekmarFotolarTB dmf where dmf.UrunId=u.UrunId and dmf.Sira=1) as Webp,
                                            (select dmf.Image from DepoUrunKart_MekmarFotolarTB dmf where dmf.UrunId=u.UrunId and dmf.Sira=1) as Jpeg

                                            from DepoUrunKartTB k,DepoUrunKart_MekmarSiteTB u
                                            where MekmarSite=1 and u.UrunId=k.ID and u.TurkeyStock=0
                                            and u.Yayinla=1
                                        
                                        """)
            
            liste = list()
            for item in products:
                model = UrunlerModel()
                model.id = item.ID          
                model.stok = item.Stok_Sqft
                model.fiyat = item.Fiyat 
                model.imagePath = 'https://cdn.mekmarimage.com/usa-products/' + item.Webp
                model.macPath = 'https://cdn.mekmarimage.com/usa-products/' + item.Jpeg
                model.oran = self.__getOran(model.stok,model.maxStock)
                model.size = item.Size
                model.urunadi_en = item.urunadi_en
                model.urunadi_fr = item.urunadi_fr
                model.urunadi_es = item.urunadi_es
                model.photos = []

            
                liste.append(model)
        
            schema = UrunlerSchema(many=True)
        
            return sorted(schema.dump(liste),key=lambda x:x['stok'],reverse=True)
                
            
        except Exception as e:
            print('getProductList hata ',str(e))
            return False

    def getCategoryProductList(self,name):
        try:
            name = name.replace('-',' ')
            products = self.sql.getStoreList("""
                                            Select
                                            k.ID,
                                            u.Fiyat,
                                            u.MaxStock,
                                            dbo.get_YeniDepoStok(k.ID,k.Devir) * k.KutuSqft as Stok_Sqft,
                                            u.Size,
                                            u.Sira,
                                            u.urunadi_en,
                                            u.aciklama_en,
                                            u.urunadi_fr,
                                            u.aciklama_fr,
                                            u.urunadi_es,
                                            u.aciklama_es,
                                            (select dmf.Webp from DepoUrunKart_MekmarFotolarTB dmf where dmf.UrunId=u.UrunId and dmf.Sira=1) as Webp,
                                            (select dmf.Image from DepoUrunKart_MekmarFotolarTB dmf where dmf.UrunId=u.UrunId and dmf.Sira=1) as Jpeg

                                            from DepoUrunKartTB k,DepoUrunKart_MekmarSiteTB u
                                            where MekmarSite=1 and u.UrunId=k.ID and u.TurkeyStock=0 and dbo.Get_KategoriAdi(k.UrunKartID) = ?
                                            and u.Yayinla=1
                                        
                                        """,(name))
            
            liste = list()
            index = 0
            for item in products:
                model = UrunlerModel()
                model.id = item.ID   
                model.index = index       
                model.stok = item.Stok_Sqft
                model.fiyat = item.Fiyat 
                model.imagePath = 'https://cdn.mekmarimage.com/usa-products/' + item.Webp
                model.macPath = 'https://cdn.mekmarimage.com/usa-products/' + item.Jpeg
                model.oran = self.__getOran(model.stok,model.maxStock)
                model.size = item.Size
                model.urunadi_en = item.urunadi_en
                model.urunadi_fr = item.urunadi_fr
                model.urunadi_es = item.urunadi_es
                index+=1

            
                liste.append(model)
        
            schema = UrunlerSchema(many=True)
        
            return sorted(schema.dump(liste),key=lambda x:x['stok'],reverse=True)
                
            
        except Exception as e:
            print('getProductList hata ',str(e))
            return False


    def getProductOutofStockList(self):
        try:
            products = self.sql.getList("""
                                            Select            
                                            k.ID,
                                            u.Fiyat,			
                                            u.MaxStock,
                                            u.urunadi_en,
                                        u.aciklama_en,
                                        u.urunadi_fr,
                                        u.aciklama_fr,
                                            u.urunadi_es,
                                        u.aciklama_es,
                                            dbo.get_YeniDepoStok(k.ID,k.Devir) * k.KutuSqft as Stok_Sqft,
                                            u.Size,
                                            u.Sira
                                            from DepoUrunKartTB k,DepoUrunKart_MekmarSiteTB u
                                        where MekmarSite=1 and u.UrunId=k.ID and u.TurkeyStock=1
                                            and u.Yayinla=1
                                            order by u.Sira asc
                                        
                                        """)
            
            liste = list()
            for item in products:
                model = UrunlerModel()
                model.id = item.ID          
                model.stok = item.Stok_Sqft
                model.fiyat = item.Fiyat 
                model.imagePath,model.macPath = self.__getFoto(model.id)
                # model.imagePath = 'https://cdn.mekmarimage.com/usa-products/' + item.Webp
                # model.macPath = 'https://cdn.mekmarimage.com/usa-products/' + item.Jpeg
                model.oran = self.__getOran(model.stok,model.maxStock)
                model.size = item.Size
                model.urunadi_en = item.urunadi_en
                model.urunadi_fr = item.urunadi_fr
                model.urunadi_es = item.urunadi_es
                model.photos = []

            
                liste.append(model)
        
            schema = UrunlerSchema(many=True)
        
            return sorted(schema.dump(liste),key=lambda x:x['stok'],reverse=True)
                
            
        except Exception as e:
            print('getProductOutofStockList hata ',str(e))
            return False
    
    def getUsageAreasList(self):
        try:
            usageList = self.sql.getList("""
                                            select
                                            k.Id,
                                            k.kullanim_en,
                                            k.kullanim_fr,
                                            k.kullanim_es,
                                            count(*) as UrunSayisi
                                            from
                                            DepoUrunKart_Urun_KullanimTB u,DepoUrunKart_UsaKullanimAlanTB k
                                            where
                                            u.KullanimId=k.Id
                                            group by k.Id,k.kullanim_en,kullanim_fr,kullanim_es
                                            order by count(*) desc
                                         
                                         """)

            liste = list()
            for item in usageList:
                model = CardListModel()
                model.name = item.kullanim_en
                model.name_fr = item.kullanim_fr
                model.name_es = item.kullanim_es
                model.value = item.UrunSayisi
                model.link = '/usa/usaStock/' + str(model.name).replace(' ','-')
                liste.append(model)
            schema = CardListSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('usageAreasList hata',str(e))
            return False
        
        
    def getColorList(self):
        try:
            colorList = self.sql.getList("""
                                            select
                                            k.renk_en,
                                            k.renk_fr,
                                            k.renk_es,
                                            count(*) as UrunSayisi
                                            from
                                            DepoUrunKartTB d,DepoUrunKart_MekmarSiteTB k
                                            where
                                            d.MekmarSite=1 and k.UrunId = d.ID
                                            and k.Yayinla=1
                                            group by k.renk_en,k.renk_fr,k.renk_es
                                            order by count(*) desc
                                         
                                         """)

            liste = list()
            for item in colorList:
                model = CardListModel()
                model.name = item.renk_en
                model.name_fr = item.renk_fr
                model.name_es = item.renk_es
                model.value = item.UrunSayisi
                model.link = '/usa/Color/' + str(model.name).replace(' ','-')
                liste.append(model)
            schema = CardListSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getColorList hata',str(e))
            return False
        
    def getSizeList(self):
        try:
            sizeList = self.sql.getList("""
                                            select
                                            m.Size,
                                            m.LinkSize,
                                            count(*) as UrunSayisi
                                            from
                                            DepoUrunKartTB d,DepoUrunKart_MekmarSiteTB m
                                            where
                                            d.MekmarSite=1 and m.UrunId = d.ID
                                            and MosaicSize=0 and m.Yayinla=1
                                            group by m.Size,m.LinkSize 
                                            order by count(*) desc
                                         
                                         """)

            liste = list()
            for item in sizeList:
                model = CardListModel()
                model.name = item.Size
                model.name_fr = item.Size
                model.name_es = item.Size
                model.value = item.UrunSayisi
                model.link = '/usa/Size/' + str(item.LinkSize)
                liste.append(model)
            schema = CardListSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getSizeList hata',str(e))
            return False
    
    def getProductDetailList(self,id):
        try:
            productDetail = self.sql.getStoreList("""
                                    select
                                            k.ID,
                                            k.SkuNo,
                                            u.Fiyat,
                                            u.MaxStock,
                                            dbo.get_YeniDepoStok(k.ID,k.Devir) * k.KutuSqft as Stok_Sqft,
                                            u.Size,
                                            u.Sira,
                                            u.urunadi_en,
                                            u.aciklama_en,
                                            u.urunadi_fr,
                                            u.aciklama_fr,
                                            u.urunadi_es,
                                            u.aciklama_es,
                                            k.KutuAdet,
											k.KutuSqft,
											k.KasaKutu,
											k.KasaSqft,
											u.Surface,
                                            u.aciklama_en,
											u.aciklama_fr,
											u.aciklama_es,
                                            (select dmf.Webp from DepoUrunKart_MekmarFotolarTB dmf where dmf.UrunId=u.UrunId and dmf.Sira=1) as Webp,
                                            (select dmf.Image from DepoUrunKart_MekmarFotolarTB dmf where dmf.UrunId=u.UrunId and dmf.Sira=1) as Jpeg

                                            from DepoUrunKartTB k,DepoUrunKart_MekmarSiteTB u
                                            where MekmarSite=1 and u.UrunId=k.ID and k.ID=?
                                            and u.Yayinla=1
                                  
                                  
                                  """,(id))
            
            liste = list()
            for item in productDetail:
                model = UrunlerModel()
                model.id = item.ID       
                model.skuNo = item.SkuNo   
                model.stok = item.Stok_Sqft
                model.fiyat = item.Fiyat 
                model.surface = item.Surface
                model.imagePath = 'https://cdn.mekmarimage.com/usa-products/' + item.Webp
                model.macPath = 'https://cdn.mekmarimage.com/usa-products/' + item.Jpeg
                model.maxStock = item.MaxStock
                model.oran = self.__getOran(model.stok,model.maxStock)
                model.size = item.Size
                model.urunadi_en = item.urunadi_en
                model.urunadi_fr = item.urunadi_fr
                model.urunadi_es = item.urunadi_es
                model.aciklama_en = item.aciklama_en
                model.aciklama_fr = item.aciklama_fr
                model.aciklama_es = item.aciklama_es
                
                lbs = round((float(item.KutuSqft) * 6.0498),0)
                lbsKasa = round((float(item.KasaSqft) * 6.0139),0)
                model.kutudetay_en = "Per Box: " + str(item.KutuAdet) +  ' tiles, ' + str(round(item.KutuSqft,2)) + " sq ft, " + str(lbs) +  " lbs."
                model.kasadetay_en = "Per Crate: " + str(item.KasaKutu) +  " boxes, " + str(round(item.KasaSqft,2)) +  " sq ft, " +str(lbsKasa) + " lbs."
                model.kutudetay_fr = "Par Boîte: " + str(item.KutuAdet) +  ' carrelage, ' + str(round(item.KutuSqft,2)) + " pieds carrés, " + str(lbs) +  " livres."
                model.kasadetay_fr = "Par Caisse: " + str(item.KasaKutu) +  " des boites, " + str(round(item.KasaSqft,2)) +  " pieds carrés, " + str(lbsKasa) + " livres."
                model.kutudetay_es = "Por Caja: " + str(item.KutuAdet) +  ' losas, ' + str(round(item.KutuSqft,2)) + " pies cuadrados, " + str(lbs) +  " la libra."
                model.kasadetay_es = "Por Caja: " + str(item.KasaKutu) +  " cajas, " + str(round(item.KasaSqft,2)) +  " pies cuadrados, " +str(lbsKasa) + " la libra."
                model.photos = self.__getFotoList(id)
                liste.append(model)
            schema = UrunlerSchema(many=True)
            return schema.dump(liste)
        
        except Exception as e:
            print('getProductDetailList',str(e))
            return False
    
    # def getTurkeyUrunList(self):
    #     dtList = self.sql.getList(
    #         """
    #          Select            
	# 		 k.ID,
	# 		 u.Fiyat,			
	# 		 u.MaxStock,
    #          u.urunadi_en,
	# 		u.aciklama_en,
	# 		u.urunadi_fr,
	# 		u.aciklama_fr,
    #         u.urunadi_es,
	# 		u.aciklama_es,
    #         dbo.get_YeniDepoStok(k.ID,k.Devir) * k.KutuSqft as Stok_Sqft,
    #         u.Size,
    #         u.Sira
    #         from DepoUrunKartTB k,DepoUrunKart_MekmarSiteTB u
	# 		where MekmarSite=1 and u.UrunId=k.ID and u.TurkeyStock=1
    #         and u.Yayinla=1
    #            order by u.Sira asc
    #         """
    #     )

    #     liste = list()
    #     for item in dtList:
    #         model = UrunlerModel()
    #         model.id = item.ID           
    #         model.stok = item.Stok_Sqft
    #         model.fiyat = item.Fiyat 
    #         model.imagePath,model.macPath = self.__getFoto(model.id)
    #         model.fotolar = self.__getFotoList(model.id)
    #         model.maxStock = item.MaxStock
    #         model.oran = self.__getOran(model.stok,model.maxStock)
    #         model.size = item.Size
    #         model.sira = item.Sira
    #         model.urunadi_en = item.urunadi_en 
    #         model.aciklama_en = item.aciklama_en

    #         model.urunadi_fr = item.urunadi_fr 
    #         model.aciklama_fr = item.aciklama_fr

    #         model.urunadi_es = item.urunadi_es
    #         model.aciklama_es = item.aciklama_es

    #         model.link = '/USAstocks/' + model.urunadi_en.replace(' ','-') + '/' + str(model.id)

    #         liste.append(model)
        
    #     schema = UrunlerSchema(many=True)

    #     return sorted(schema.dump(liste),key=lambda x:x['stok'],reverse=True)
    
    # def getOlcuListesi(self):

    #     result = self.sql.getList(
    #         """
    #         select
    #         m.Size,
    #         m.LinkSize,
    #         count(*) as UrunSayisi
    #         from
    #         DepoUrunKartTB d,DepoUrunKart_MekmarSiteTB m
    #         where
    #         d.MekmarSite=1 and m.UrunId = d.ID
    #         and MosaicSize=0 and m.Yayinla=1
    #         group by m.Size,m.LinkSize 
    #         order by count(*) desc
    #         """
    #     )

    #     liste = list()

    #     id = 1

    #     for item in result:

    #         model = CardListSchema()
    #         model.id = id 
    #         model.name = item.Size 
    #         model.value = item.UrunSayisi 
    #         model.link = '/USAstocks/Size/' + item.LinkSize
            
    #         liste.append(model)

    #         id += 1

    #     schema = CardListSchema(many=True)

    #     return schema.dump(liste)
    
    # def getMosaicOlcuListesi(self):

    #     result = self.sql.getList(
    #         """
    #         select
    #         m.Size,
    #         m.LinkSize,
    #         count(*) as UrunSayisi
    #         from
    #         DepoUrunKartTB d,DepoUrunKart_MekmarSiteTB m
    #         where
    #         d.MekmarSite=1 and m.UrunId = d.ID
    #         and MosaicSize=1 and m.Yayinla=1
    #         group by m.Size,m.LinkSize
    #         order by count(*) desc
    #         """
    #     )

    #     liste = list()

    #     id = 1

    #     for item in result:

    #         model = CardListSchema()
    #         model.id = id 
    #         model.name = item.Size 
    #         model.value = item.UrunSayisi 
    #         model.link = '/USAstocks/Size/' + item.LinkSize
            
    #         liste.append(model)

    #         id += 1

    #     schema = CardListSchema(many=True)

    #     return schema.dump(liste)
    
    # def getRenkListesi(self):

    #     result = self.sql.getList(
    #         """
    #         select
    #         k.renk_en,
	# 		k.renk_fr,
    #         k.renk_es,
    #         count(*) as UrunSayisi
    #         from
    #         DepoUrunKartTB d,DepoUrunKart_MekmarSiteTB k
    #         where
    #         d.MekmarSite=1 and k.UrunId = d.ID
    #         and k.Yayinla=1
    #         group by k.renk_en,k.renk_fr,k.renk_es
    #         order by count(*) desc
    #         """
    #     )

    #     liste = list()

    #     id = 1

    #     for item in result:

    #         model = CardListSchema()
    #         model.id = id 
    #         model.name = item.renk_en 
    #         model.name_fr = item.renk_fr 
    #         model.name_es = item.renk_es
    #         model.value = item.UrunSayisi 
    #         model.link = '/USAstocks/Color/' + str(model.name).replace(' ','-')

    #         liste.append(model)
    #         id += 1

    #     schema = CardListSchema(many=True)

    #     return schema.dump(liste)
    
    # def getKategoriList(self):

    #     result = self.sql.getList(
    #         """
    #         select
    #         dbo.Get_KategoriAdi(d.UrunKartID) as Kategori,
    #         count(*) as UrunSayisi
    #         from
    #         DepoUrunKartTB d
    #         where
    #         d.MekmarSite=1
    #         group by dbo.Get_KategoriAdi(d.UrunKartID)
    #         order by count(*) desc
    #         """
    #     )

    #     liste = list()

    #     id = 1

    #     for item in result:

    #         model = CardListSchema()
    #         model.id = id 
    #         model.name = item.Kategori 
    #         model.value = item.UrunSayisi 
    #         model.link = '/USAstocks/' + str(model.name).replace(' ','-')

    #         liste.append(model)
    #         id += 1
        
    #     schema = CardListSchema(many=True) 

    #     return schema.dump(liste)
    
    # def getKullanimList(self):

    #     result = self.sql.getList(
    #         """
    #        select
	# 		k.Id,
	# 		k.kullanim_en,
	# 		k.kullanim_fr,
    #         k.kullanim_es,
	# 		count(*) as UrunSayisi
    #         from
    #         DepoUrunKart_Urun_KullanimTB u,DepoUrunKart_UsaKullanimAlanTB k
	# 		where
	# 		u.KullanimId=k.Id
	# 		group by k.Id,k.kullanim_en,kullanim_fr,kullanim_es
	# 		order by count(*) desc
            
    #         """
    #     )

    #     liste = list()
        
    #     for item in result:

    #         model = CardListModel()
    #         model.id = item.Id 
    #         model.name = item.kullanim_en
    #         model.name_fr = item.kullanim_fr 
    #         model.name_es = item.kullanim_es
    #         model.link = '/USAstocks/Areas-of-Usage/' + str(model.name).replace(' ','-')
    #         model.value = item.UrunSayisi
    #         liste.append(model)

    #     schema = CardListSchema(many=True)

    #     return schema.dump(liste)
    
    # def __getFoto(self,urunid):

    #     imagePath = ''
    #     macPath = ''
    #     try:
    #         for item in self.fotolar:
    #             if item.Sira == 1 and item.UrunId == urunid:
    #                 imagePath = 'https://cdn.mekmarimage.com/usa-products/' + item.Webp
    #                 macPath = 'https://cdn.mekmarimage.com/usa-products/' + item.Image
    #     except:
    #         print(' __getFoto Hata : ', urunid)

    #     return imagePath,macPath
    
    def __getFotoList(self,id):

        liste = list()
        index = 0
        for item in self.fotolar:
            if item.UrunId == id:
                model = FotolarModel()
                model._id = item.Id
                model.index = index
                model.imagePath = 'https://cdn.mekmarimage.com/usa-products/' + item.Webp 
                model.macPath = 'https://cdn.mekmarimage.com/usa-products/' + item.Image
                model.product_webp = 'https://cdn.mekmarimage.com/usa-products/' + item.Webp 
                model.product_jpeg = 'https://cdn.mekmarimage.com/usa-products/' + item.Image 
                model.sira = item.Sira 
                index+= 1
                liste.append(model)

        

        return sorted(liste,key=lambda x:x.sira,reverse=False)
    
    
    def __getFoto(self,urunid):

        imagePath = ''
        macPath = ''
        try:
            for item in self.fotolar:
                if item.Sira == 1 and item.UrunId == urunid:
                    imagePath = 'https://cdn.mekmarimage.com/usa-products/' + item.Webp
                    macPath = 'https://cdn.mekmarimage.com/usa-products/' + item.Image
        except:
            print(' __getFoto Hata : ', urunid)

        return imagePath,macPath
    
    
    def __getOran(self,stok,maxstok):

        oran = 0
        try:
            sonuc = round(((stok / maxstok)*100),0)
            if sonuc > 100:
                oran = 100
            else:
                oran = sonuc
        except:
            oran = 0
        
        print('Oran : ', oran)
        return oran