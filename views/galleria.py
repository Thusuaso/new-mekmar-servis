from models.galleria import *
from models.galleria_all import *

from helpers.sqlServer import SqlIslem
class Galery:

    def __init__(self):
        self.sql = SqlIslem()
        self.galleryList = self.sql.getList("""
                                                select 


                                        mg.ID,
                                        mg.Image_Jpg,
                                        mg.Product_Id,
                                        mg.FileName,
                                        mp.urunadi_en,
                                        mk.kategori_link,
                                        dbo.getMekmar_Finish_Link(mg.Product_Id) as Finish,
										mg.Sira,
                                        mg.Project_Id


                                    from MekmarCom_Galleria mg
                                        inner join MekmarCom_Products mp on mp.urunid = mg.Product_Id
                                        inner join MekmarCom_Kategoriler mk on mk.Id = mp.kategori_id


                                            
                                            """)
    
    def getGaleryPhotosList(self):
        try:
            result = self.sql.getList("""
                                        select * from MekmarCom_Galleria_ProjectTB

                                      
                                      """)
            liste = list()
            for item in result:
                model = GalleryProjectModel()
                model.id = item.ID
                model.project_id = item.Project_Id
                model.project_name = item.Project_Name
                model.project_image_link = item.Project_Image_Link
                model.photosList = self.__getGalleryList(item.Project_Id)
                liste.append(model)
            
            schema = GalleryProjectSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getGaleryPhotosList hata',str(e))
            return False
        
    def __getGalleryList(self,project_id):
        liste = list()
        for item in self.galleryList:
            if(item.Project_Id == project_id):
                model = GalleryPhotosAllModel()
                model.id = item.ID
                model.image_link = item.Image_Jpg
                model.product_name = item.urunadi_en
                model.sira = item.Sira
                
                model.product_id = item.Product_Id
                model.file_name = item.FileName
                model.product_link = "https://www.mekmar.com/Product/" + item.Finish + '/' + item.kategori_link + '/' + item.urunadi_en.replace(' ', '-') + '/' + str(item.Product_Id)
                liste.append(model)
            else:
                continue
        return liste    
            
                