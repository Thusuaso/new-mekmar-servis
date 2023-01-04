from marshmallow import Schema,fields
from models.mekmarpanel.fotolar import FotolarSchema,FotolarModel
from models.mekmarpanel.ebatlar import EbatlarSchema
from models.mekmarpanel.kategori import KategoriSchema,KategoriModel
from models.mekmarpanel.seramikSimge import SeramikSimgeModel,SeramikSimgeSchema
from models.mekmarpanel.cardList import CardListSchema,CardListModel


class UrunlerSchema(Schema):
    _id = fields.String()
    urunadi_en = fields.String()
    aciklama_en = fields.String()
    anahtarlar_en = fields.String()
    renk_en = fields.String()
    urunadi_fr = fields.String()
    aciklama_fr = fields.String()
    anahtarlar_fr = fields.String()
    renk_fr = fields.String()
    urunadi_es = fields.String()
    aciklama_es = fields.String()
    anahtarlar_es = fields.String()
    renk_es = fields.String()
    urunid = fields.Int()
    kategori_id = fields.Int()
    yayinla = fields.Boolean()
    tedarikciadi = fields.String()
    sira = fields.Int()
    birim = fields.String()
    urunkod = fields.String()
    #custom alanlar
    link = fields.String()
    foto = fields.String()
    imagePath = fields.String()
    macPath = fields.String()

    endusukfiyat = fields.Float()
    enyuksekfiyat = fields.Float()
    fotolar = fields.Nested(FotolarSchema(many=True))
    ebatlar = fields.Nested(EbatlarSchema(many=True))
    ebatList1 = fields.Nested(EbatlarSchema(many=True))
    ebatList2 = fields.Nested(EbatlarSchema(many=True))
    kenarislem = fields.String()
    kenarIslemList = fields.Nested(CardListSchema(many=True))
    kenarIslemList_fr = fields.Nested(CardListSchema(many=True))
    kenarIslemList_es = fields.Nested(CardListSchema(many=True))
    kategori = fields.Nested(KategoriSchema)
    seramikSimgeList = fields.Nested(SeramikSimgeSchema(many=True))
    benzerUrunLink = fields.String()
    testrapor = fields.String()

    fotoWeb = fields.String()
    usaListele = fields.Boolean()
    kasaDetay = fields.String()
    kutuDetay = fields.String()
    surface = fields.String()
    edge = fields.String()
    usafiyat = fields.Float()
    usaebat = fields.String()
    kategoriadi = fields.String()
    stonetype = fields.Int()

class UrunlerModel:
    _id = ""
    urunadi_en = ""
    aciklama_en = ""
    anahtarlar_en = ""
    renk_en = ""
    urunadi_fr = ""
    aciklama_fr = ""
    anahtarlar_fr = ""
    renk_fr = ""
    urunadi_es = ""
    aciklama_es = ""
    anahtarlar_es = ""
    renk_es = ""
    urunid = None
    kategori_id = None
    yayinla = False
    tedarikciadi = ""
    sira = None
    birim = ""
    urunkod = ""
    link = ""
    #custom alanlar
    foto = ""
    endusukfiyat = None
    fotolar = list()
    ebatlar = list()
    ebatList1 = list()
    ebatList2 = list()
    kenarislem  = ""
    kenarIslemList = list()
    kenarIslemList_fr = list()
    kenarIslemList_es = list()
    imagePath = ""
    macPath = ""
    kategori = KategoriModel()
    seramikSimgeList = list()
    benzerUrunLink = ''
    fotoWeb = ""
    enyuksekfiyat = 0
    testrapor = ""
    usaListele = False
    kasaDetay = ""
    kutuDetay = ""
    surface = ""
    edge = ""
    usafiyat = 0 
    usaebat = ""
    kategoriadi = ""
    stonetype=None
   
   
  