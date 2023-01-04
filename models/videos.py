from marshmallow import Schema,fields

class VideosSchema(Schema):
    id = fields.Int()
    videoUrl =  fields.String()
    title =  fields.String()
    category =  fields.Int()
    isFrance = fields.Boolean()
    
class VideosModel:
    id = 0
    videoUrl =  ""
    title =  ""
    category =  0
    isFrance = False
    
    
    