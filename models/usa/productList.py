from marshmallow import Schema,fields
from models.usa.photos import * 

class UrunlerSchema(Schema):
    index = fields.Int()
    id = fields.Int()
    urunadi = fields.String()
    aciklama = fields.String()
    fiyat = fields.Float()
    stok = fields.Float()
    imagePath = fields.String()
    macPath = fields.String()
    link = fields.String()
    maxStock = fields.Float()
    oran = fields.Int()
    skuNo = fields.String()
    size = fields.String()
    kutuDetay = fields.String()
    kasaDetay = fields.String()
    sira = fields.Int()
    surface = fields.String()
    edge = fields.String()
    turkeyStock = fields.Boolean()
    urunadi_en = fields.String()
    aciklama_en = fields.String()
    aciklama_en = fields.String()
    anahtarlar_en = fields.String()
    renk_en = fields.String()
    kutudetay_en = fields.String()
    kasadetay_en = fields.String()
    surface_en = fields.String()
    edge_en = fields.String()
    
    urunadi_fr = fields.String()
    aciklama_fr = fields.String()
    anahtarlar_fr = fields.String()
    renk_fr = fields.String()
    kutudetay_fr = fields.String()
    kasadetay_fr = fields.String()
    surface_fr = fields.String()
    edge_fr = fields.String()

    urunadi_es = fields.String()
    aciklama_es = fields.String()
    anahtarlar_es = fields.String()
    renk_es = fields.String()
    kutudetay_es = fields.String()
    kasadetay_es = fields.String()
    surface_es = fields.String()
    edge_es = fields.String()
    
    photos = fields.Nested(FotolarSchema(many=True))

class UrunlerModel:
    index = 0
    id = None 
    urunadi = ""
    aciklama = ""
    fiyat = 0
    stok = 0
    imagePath = ""
    macPath = ""
    link = ""
    maxStock = 0
    oran = 0
    skuNo = ""
    size = ""
    kutuDetay = ""
    kasaDetay = ""
    sira = 0
    surface = ""
    edge = ""
    turkeyStock = False
    urunadi_en = ""
    aciklama_en = ""
    anahtarlar_en = ""
    renk_en = ""
    kutudetay_en = ""
    kasadetay_en = ""
    surface_en = ""
    edge_en = ""

    urunadi_fr = ""
    aciklama_fr = ""
    anahtarlar_fr = ""
    renk_fr = ""
    kutudetay_fr = ""
    kasadetay_fr = ""
    surface_fr = ""
    edge_fr = ""

    urunadi_es = ""
    aciklama_es = ""
    anahtarlar_es = ""
    renk_es = ""
    kutudetay_es = ""
    kasadetay_es = ""
    surface_es = ""
    edge_es = ""

    photos = []

