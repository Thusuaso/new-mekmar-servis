from marshmallow import Schema,fields

class SliderListSchema(Schema):
    id = fields.Int()
    slide_no = fields.Int()
    slide_jpeg = fields.String()
    slide_webp = fields.String()
    slide_jpeg_fr = fields.String()
    slide_webp_fr = fields.String()
    slide_jpeg_es = fields.String()
    slide_webp_es = fields.String()
    
    
    slide_name = fields.String()
    slide_name_fr = fields.String()
    slide_name_es = fields.String()

    
class SliderListModel:
    id = 0
    slide_no = 0
    slide_jpeg = ""
    slide_webp = ""
    slide_jpeg_fr = ""
    slide_webp_fr = ""
    slide_jpeg_es = ""
    slide_webp_es = ""
    slide_name = ""
    slide_name_fr = ""
    slide_name_es = ""
    

    
    
    