from helpers.sqlServer import SqlConnect
from models.slider import *
class Slider:
    def __init__(self):
        self.sql = SqlConnect().data
        
    def getSliderOneList(self):
        try:
            sliderList = self.sql.getList("""
                                                select 
                                                    * 
                                                from 
                                                    Mekmar_Com_Slide_Fotoları where SlideNo=1
                                            
                                            """)
            slideOne = list()
            for item in sliderList:
                model = SliderListModel()
                model.id = item.ID
                model.slide_no = item.SlideNo
                model.slide_jpeg = "https://mekmar-image.fra1.digitaloceanspaces.com/slides/slide2/" + item.Jpeg
                model.slide_webp = "https://mekmar-image.fra1.digitaloceanspaces.com/slides/slide2/" + item.Webp
                model.slide_name = item.urunAdi
                model.slide_name_fr = item.urunAdiFr
                model.slide_name_es = item.urunAdiEs
                slideOne.append(model)
            schema = SliderListSchema(many=True)
            return schema.dump(slideOne)
                
        
        except Exception as e:
            print("getSliderOneList hata",str(e))
            return False
    
    
    def getSliderTwoList(self):
        try:
            sliderList = self.sql.getList("""
                                                select 
                                                    * 
                                                from 
                                                    Mekmar_Com_Slide_Fotoları where SlideNo=2
                                            
                                            """)
            slideTwo = list()
            for item in sliderList:
                model = SliderListModel()
                model.id = item.ID
                model.slide_no = item.SlideNo
                model.slide_jpeg = "https://mekmar-image.fra1.digitaloceanspaces.com/slides/slide1/" + item.Jpeg
                model.slide_webp = "https://mekmar-image.fra1.digitaloceanspaces.com/slides/slide1/" + item.Webp
                model.slide_name = item.urunAdi
                model.slide_name_fr = item.urunAdiFr
                model.slide_name_es = item.urunAdiEs
                slideTwo.append(model)
            schema = SliderListSchema(many=True)
            return schema.dump(slideTwo)
                
        
        except Exception as e:
            print("getSliderTwoList hata",str(e))
            return False
    
    def getSliderThreeList(self):
        try:
            sliderList = self.sql.getList("""
                                                select 
                                                    * 
                                                from 
                                                    Mekmar_Com_Slide_Fotoları where SlideNo=3
                                            
                                            """)
            slideThree = list()
            for item in sliderList:
                model = SliderListModel()
                model.id = item.ID
                model.slide_no = item.SlideNo
                model.slide_jpeg = "https://mekmar-image.fra1.digitaloceanspaces.com/slides/slide3/" + item.Jpeg
                model.slide_webp = "https://mekmar-image.fra1.digitaloceanspaces.com/slides/slide3/" + item.Webp
                model.slide_name = item.urunAdi
                model.slide_name_fr = item.urunAdiFr
                model.slide_name_es = item.urunAdiEs
                slideThree.append(model)
            schema = SliderListSchema(many=True)
            return schema.dump(slideThree)
                
        
        except Exception as e:
            print("getSliderThreeList hata",str(e))
            return False
    
    def getSliderFourList(self):
        try:
            sliderList = self.sql.getList("""
                                                select * from DepoUrunKart_MekmarSlideTB
                                            
                                            """)
            slideThree = list()
            for item in sliderList:
                model = SliderListModel()
                model.id = item.Id
                model.slide_no = item.Sira
                model.slide_jpeg = "https://cdn.mekmarimage.com/usa-slide/" + item.Image
                model.slide_webp = "https://cdn.mekmarimage.com/usa-slide/" + item.Webp
                model.slide_jpeg_fr = "https://cdn.mekmarimage.com/usa-slide/fr/" + item.Image
                model.slide_webp_fr = "https://cdn.mekmarimage.com/usa-slide/fr/" + item.Webp
                model.slide_jpeg_es = "https://cdn.mekmarimage.com/usa-slide/es/" + item.Image
                model.slide_webp_es = "https://cdn.mekmarimage.com/usa-slide/es/" + item.Webp
                model.slide_name = item.Name
                slideThree.append(model)
            schema = SliderListSchema(many=True)
            return schema.dump(slideThree)
                
        
        except Exception as e:
            print("getSliderThreeList hata",str(e))
            return False
      
        
    