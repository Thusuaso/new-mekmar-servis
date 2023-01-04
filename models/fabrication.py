from marshmallow import Schema,fields

class FabricationSchema(Schema):
    id = fields.Int()
    titleEn = fields.String()
    titleFr = fields.String()
    titleEs = fields.String()
    webpS = fields.String()
    jpegS = fields.String()
    webpB = fields.String()
    jpegB = fields.String()
    line = fields.Int()
    
class FabricationModel:
    id = 0
    titleEn = ""
    titleFr = ""
    titleEs = ""
    webpS = ""
    jpegS = ""
    webpB = ""
    jpegB = ""
    line = 0
    
    
    