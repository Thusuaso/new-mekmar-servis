from marshmallow import Schema,fields


class OnerilenUrunlerSchema(Schema):
    id = fields.Int()
    urunid = fields.Int()
    onerilenurunid = fields.Int()
    benzerurunid = fields.Int()
    imagePath = fields.String()
    macPath = fields.String()
    link = fields.String()
    urunadi_en = fields.String()
    urunadi_fr = fields.String()
    urunadi_es = fields.String()
    nocdn = fields.String()

class OnerilenUrunlerModel:
    id = None 
    urunid = None 
    onerilenurunid = None
    benzerurunid = None
    imagePath = ""
    macPath = ""
    link = ""
    urunadi_en = ""
    urunadi_fr = ""
    urunadi_es = ""
    nocdn = ""