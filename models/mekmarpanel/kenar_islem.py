from marshmallow import Schema,fields


class KenarIslemSchema(Schema):
    _id = fields.String()
    islemadi = fields.String()
    islemadi_es = fields.String()
    islemadi_fr = fields.String()
    dil = fields.String()
    kategori_id = fields.Int()
    urunid = fields.Int()
    #custom alan
    urunSayisi = fields.Int()
    renk_css = fields.String()

class KenarIslemModel:
    _id = ""
    islemadi = ""
    islemadi_es = ""
    islemadi_fr = ""
    dil = ""
    kategori_id = None
    urunid = None
    urunSayisi = None
    renk_css = ""