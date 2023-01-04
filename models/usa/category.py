from marshmallow import Schema,fields

class UsaCategoryListSchema(Schema):
    id = fields.Int()
    category_en = fields.String()
    category_fr = fields.String()
    category_es = fields.String()
    category_produt_count = fields.Int()
    category_link = fields.String()
    
    
class UsaCategoryListModel:
    id = 0
    category_en = ""
    category_fr = ""
    category_es = ""
    category_produt_count = 0
    category_link = ""

    
    
    