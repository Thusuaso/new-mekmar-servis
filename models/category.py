from marshmallow import Schema,fields

class MainPageCategorySchema(Schema):
    category_id = fields.String()
    category_en = fields.String()
    category_fr = fields.String()
    category_es = fields.String()
    category_link = fields.String()
    category_foto_en = fields.String()
    category_foto_fr = fields.String()
    category_foto_es = fields.String()
    category_sira = fields.Int()
    
class MainPageCategoryModel:
    category_id = 0
    category_en = ""
    category_fr = ""
    category_es = ""
    category_link = ""
    category_foto_en = ""
    category_foto_fr = ""
    category_foto_es = ""
    category_sira = 0
    
    
    