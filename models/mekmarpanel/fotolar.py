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