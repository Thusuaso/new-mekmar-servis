from marshmallow import Schema,fields

class CategoryDetailSchema(Schema):
    id = fields.Int()
    productId = fields.Int()
    categoryId = fields.Int()
    productNameEn = fields.String()
    productNameFr = fields.String()
    productNameEs = fields.String()
    productColorEn = fields.String()
    productColorFr = fields.String()
    productColorEs = fields.String()
    webp = fields.String()
    jpeg = fields.String()
    productLink = fields.String()

    
class CategoryDetailModel:
    id = 0
    productId = 0
    categoryId = 0
    productNameEn = ""
    productNameFr = ""
    productNameEs = ""
    productColorEn = ""
    productColorFr = ""
    productColorEs = ""
    webp = ""
    jpeg = ""
    productLink:""
    
    
    