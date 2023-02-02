from marshmallow import Schema,fields

class CategoryProductDetailSchema(Schema):
    product_name_en = fields.String()
    product_name_fr = fields.String()
    product_name_es = fields.String()
    product_description_en = fields.String()
    product_description_fr = fields.String()
    product_description_es = fields.String()
    product_color_en = fields.String()
    product_color_fr = fields.String()
    product_color_es = fields.String()
    product_test_rapor = fields.String()
    product_code = fields.String()
    product_queue = fields.Int()
    product_unit = fields.String()
    product_stoneType = fields.Int()
    
class CategoryProductDetailModel:
    product_name_en = ""
    product_name_fr = ""
    product_name_es = ""
    product_description_en = ""
    product_description_fr = ""
    product_description_es = ""
    product_color_en = ""
    product_color_fr = ""
    product_color_es = ""
    product_test_rapor = ""
    product_code = ""
    product_queue = 0
    product_unit = ""
    product_stoneType = 0
    
class CategoryProductDetailPhotosSchema(Schema):
    index= fields.Int()
    id = fields.Int()
    product_id = fields.Int()
    product_photos_name = fields.String()
    product_webp = fields.String()
    product_jpeg = fields.String()
    product_queue = fields.Int()
    
class CategoryProductDetailPhotosModel:
    index = 0
    id = 0
    product_id = 0
    product_photos_name = ""
    product_webp = ""
    product_jpeg = ""
    product_queue = ""
    
    
class CategoryProductDetailEbatsSchema(Schema):
    id = fields.Int()
    product_id = fields.Int()
    product_dimension = fields.String()
    product_unit = fields.String()
    product_price = fields.Float()

class CategoryProductDetailEbatsModel:
    id = 0
    product_id = 0
    product_dimension = ""
    product_unit = ""
    product_price = 0
    

class CategoryProductDetailSuggestedSchema(Schema):
    id = fields.Int()
    product_id = fields.Int()
    product_name_en = fields.String()
    product_name_fr = fields.String()
    product_name_es = fields.String()
    product_webp = fields.String()
    product_jpeg = fields.String()
    product_category_name = fields.String()
    product_category_link = fields.String()

    
class CategoryProductDetailSuggestedModel:
    id = 0
    product_id = 0
    product_name_en = ""
    product_name_fr = ""
    product_name_es = ""
    product_webp = ""
    product_jpeg = ""
    product_category_name = 0
    product_category_link = 0
    
