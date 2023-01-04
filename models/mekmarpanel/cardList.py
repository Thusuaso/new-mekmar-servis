from marshmallow import Schema,fields
from models.mekmarpanel.kenar_islem import *

class CardListSchema(Schema):
    id = fields.Int()
    _id = fields.String()
    name = fields.String()
    name_fr = fields.String()
    name_es = fields.String()
    value = fields.Int() 
    link = fields.String()
    link_fr = fields.String()
    link_es = fields.String()


class CardListModel:
    id = None 
    _id = ""
    name = ""
    name_fr = ""
    name_es = ""
    value = 0
    link = "" 
    link_fr = ""
    link_es = ""
