from marshmallow import Schema,fields


class KategoriSchema(Schema):
    kategoriadi_en = fields.String()
    kategoriadi_fr = fields.String()
    kategoriadi_es = fields.String()
    foto_en = fields.String()
    foto_fr = fields.String()
    foto_es = fields.String()
    kategori_id = fields.Int()
    sira = fields.Int()
    #custom alanlar
    urunSayisi = fields.Int()
    link = fields.String()
    foto_link_en = fields.String()
    foto_web_en = fields.String()
    foto_web_fr = fields.String()
    foto_web_es = fields.String()

class KategoriModel:
    kategoriadi_en = ""
    kategoriadi_fr = ""
    kategoriadi_es = ""
    foto_en = ""
    foto_fr = ""
    foto_es = ""
    kategori_id = None
    sira = None
    urunSayisi = 0
    link = ""
    foto_link_en = ""
    foto_web_en = ""
    foto_web_fr = ""
    foto_web_es = ""