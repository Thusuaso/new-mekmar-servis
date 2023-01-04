from helpers.sqlServer import SqlConnect
from models.fabrication import *

class Fabrication:
    
    def __init__(self):
        self.data = SqlConnect().data
        
    def getFabricationList(self):
        try:
            fabrication = self.data.getList("""
                                                select * from Mekmar_Com_Fabrication
                                            """)
            
            liste = list()
            for item in fabrication:
                model = FabricationModel()
                model.id = item.ID
                model.titleEn =  item.TitleEn
                model.titleFr =  item.TitleFr
                model.titleEs =  item.TitleEs
                model.webpS = item.ImageWebp
                model.jpegS = item.ImageJpeg
                model.webpB = item.ImageWebpB
                model.jpegB = item.ImageJpegB
                model.line = item.Category
                liste.append(model)
                
            schema = FabricationSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print("getFabricationList",str(e))
            return False
                
                
                