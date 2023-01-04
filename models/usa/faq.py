from marshmallow import fields,Schema

class FaqListSchema(Schema):
    question_en = fields.String()
    question_fr = fields.String()
    answer_en = fields.String()
    answer_fr = fields.String()
    
    
class FaqListModel:
    question_en = ""
    question_fr = ""
    answer_en = ""
    answer_fr = ""
    