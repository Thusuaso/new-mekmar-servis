from marshmallow import Schema,fields



class FotolarSchema(Schema):
    _id = fields.String()
    id = fields.Int()
    urunid = fields.Int()
    foto = fields.String()
    imagePath = fields.String()
    macPath = fields.String()
    nocdn = fields.String()
    sira = fields.Int()
    fotoWeb = fields.String()
    name = fields.String()
    product_jpeg = fields.String()
    product_webp = fields.String()
    index = fields.Int()

class FotolarModel:
    _id = ""
    id = None
    urunid = None
    foto = ""
    sira = None
    imagePath = ""
    macPath = ""
    fotoWeb = ""
    nocdn = ""
    name = ""
    product_jpeg = ""
    product_webp = ""
    index = 0