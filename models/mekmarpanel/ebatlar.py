from marshmallow import Schema,fields
from models.mekmarpanel.cardList import CardListSchema,CardListModel

class EbatlarSchema(Schema):
    _id = fields.String()
    id = fields.Int()
    urunid = fields.Int()
    ebat = fields.String()
    #birim = fields.String()
    fiyat = fields.Float()
    #alis = fields.Float()
    #aciklama = fields.String()


class EbatlarModel:
    _id  = ""
    id = None
    urunid = None
    ebat = ""
    #birim = ""
    fiyat = None
    #alis = None
    #aciklama = None

