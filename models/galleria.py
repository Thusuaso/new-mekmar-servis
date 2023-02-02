from marshmallow import Schema,fields
from models.galleria_all import GalleryPhotosAllSchema
class GalleryPhotosSchema(Schema):
    id = fields.Int()
    image_link = fields.String()
    product_name = fields.String()
    product_id = fields.Int()
    file_name = fields.String()
    product_link = fields.String()
    sira = fields.String()
    
    
class GalleryPhotosModel:
    id = 0
    image_link = ""
    product_name = ""
    product_id= 0
    file_name = ""
    product_link = ""
    sira = 1
    photosList = list()
    
class GalleryProjectSchema(Schema):
    id = fields.Int()
    project_id = fields.Int()
    project_name = fields.String()
    project_image_link = fields.String()
    photosList = fields.Nested(GalleryPhotosAllSchema,many=True)
class GalleryProjectModel:
    id = 0
    project_id = 0
    project_name = ""
    project_image_link = ""
    photosList = list()