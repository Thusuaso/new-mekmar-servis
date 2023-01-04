from helpers.sqlServer import SqlConnect
from models.usa.filters import *
class Filters():
    
    def __init__(self):
        self.sql = SqlConnect().data
        
    def getUsageOfAreaProductList(self,name):
        try:
            name = name.replace('-',' ')
            usageAreaList = self.sql.getStoreList("""
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
                                                        (select dmf.Image from DepoUrunKart_MekmarFotolarTB dmf where dmf.UrunId=u.UrunId and dmf.Sira=1) as Jpeg,
                                                        dku.kullanim_en,
                                                        dku.kullanim_fr,
                                                        dku.kullanim_es,
                                                        dku.KullanimAlan

                                                        from DepoUrunKartTB k,DepoUrunKart_MekmarSiteTB u,DepoUrunKart_Urun_KullanimTB dk,DepoUrunKart_UsaKullanimAlanTB dku
                                                        where MekmarSite=1 and u.UrunId=k.ID and u.TurkeyStock=0 and k.ID = dk.UrunId and dk.KullanimId = dku.Id and KullanimAlan=?
                                                        and u.Yayinla=1

                                                  
                                                  """,(name))
            
            liste = list()
            for item in usageAreaList:
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
                

            
                liste.append(model)
        
            schema = UrunlerSchema(many=True)
        
            return sorted(schema.dump(liste),key=lambda x:x['stok'],reverse=True)
        except Exception as e:
            print('getUsageOfAreaProductList hata',str(e))
            return False
    
    def getColorProductList(self,name):
        try:
            name = name.replace('-',' ')
            usageAreaList = self.sql.getStoreList("""
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
                                                        where MekmarSite=1 and u.UrunId=k.ID and u.TurkeyStock=0 and u.renk_en=?
                                                        and u.Yayinla=1

														select * from DepoUrunKartTB

                                                  
                                                  """,(name))
            
            liste = list()
            for item in usageAreaList:
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
                

            
                liste.append(model)
        
            schema = UrunlerSchema(many=True)
        
            return sorted(schema.dump(liste),key=lambda x:x['stok'],reverse=True)
        except Exception as e:
            print('getUsageOfAreaProductList hata',str(e))
            return False
    
    def getSizeProductList(self,name):
        try:
            sizeAreaList = self.sql.getStoreList("""
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
                                                        where MekmarSite=1 and u.UrunId=k.ID and u.TurkeyStock=0 and u.LinkSize=?
                                                        and u.Yayinla=1


                                                  
                                                  """,(name))
            
            liste = list()
            for item in sizeAreaList:
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
                

            
                liste.append(model)
        
            schema = UrunlerSchema(many=True)
        
            return sorted(schema.dump(liste),key=lambda x:x['stok'],reverse=True)
        except Exception as e:
            print('getSizeProductList hata',str(e))
            return False
    
      
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