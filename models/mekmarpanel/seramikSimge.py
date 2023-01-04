from marshmallow import Schema,fields



class SeramikSimgeSchema(Schema):
    id = fields.Int()
    isim = fields.String()
    name = fields.String()
    path = fields.String()
    macPath = fields.String()


class SeramikSimgeModel:
    id = None
    isim = ""
    name = ""
    path = ""
    macPath = ""