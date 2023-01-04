from marshmallow import Schema,fields

class CategoryDetailColorSchema(Schema):
    color_en = fields.String()
    color_fr = fields.String()
    color_es = fields.String()
    color_en_count = fields.Int()
    color_fr_count = fields.Int()
    color_es_count = fields.Int()
    color_sum = fields.Int()

    
class CategoryDetailColorModel:
    color_en = ""
    color_fr = ""
    color_es = ""
    color_en_count = 0
    color_fr_count = 0
    color_es_count = 0
    color_sum = 0
    
    
class CategoryDetailFinishSchema(Schema):
    finish_en = fields.String()
    finish_fr = fields.String()
    finish_es = fields.String()
    finish_count = fields.Int()

    
class CategoryDetailFinishModel:
    finish_en = ""
    finish_fr = ""
    finish_es = ""
    finish_count = 0
    
    
    