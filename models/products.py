from marshmallow import Schema,fields

class ProductsListSchema(Schema):
    id = fields.Int()
    category_en = fields.String()
    category_fr = fields.String()
    category_es = fields.String()

    
class ProductsListModel:
    id = 0
    category_en = ""
    category_fr = ""
    category_es = ""

    
    
    