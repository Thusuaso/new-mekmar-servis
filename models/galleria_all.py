from marshmallow import Schema,fields
class GalleryPhotosAllSchema(Schema):
    id = fields.Int()
    image_link = fields.String()
    product_name = fields.String()
    product_id = fields.Int()
    file_name = fields.String()
    product_link = fields.String()
    sira = fields.String()
    
class GalleryPhotosAllModel:
    id = 0
    image_link = ""
    product_name = ""
    product_id= 0
    file_name = ""
    product_link = ""
    sira = 1