from helpers.sqlServer import SqlConnect
from models.videos import *

class Videos:
    
    def __init__(self):
        self.data = SqlConnect().data
        
    def getVideosList(self):
        try:
            videos = self.data.getList("""
                                                select * from Mekmar_Com_Videos
                                            """)
            
            liste = list()
            for item in videos:
                model = VideosModel()
                model.id = item.ID
                model.videoUrl =  item.videoURL
                model.title =  item.title
                model.category =  item.categoryID
                model.isFrance = item.isFrance

                liste.append(model)
                
            schema = VideosSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print("getFabricationList",str(e))
            return False
                
                
                