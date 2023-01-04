from models.usa.faq import *
from helpers.sqlServer import SqlConnect 
class Faq():
    
    def __init__(self):
        self.sql = SqlConnect().data
        
    def getFaqList(self):
        try:
            faqList = self.sql.getList("""
                                        select * from DepoUrunKart_Usa_SoruCevapTB
                                       """)
            liste = list()
            for item in faqList:
                model = FaqListModel()
                model.question_en = item.soru_en
                model.question_fr = item.soru_fr
                model.answer_en = item.cevap_en
                model.answer_fr = item.cevap_fr
                liste.append(model)
            schema = FaqListSchema(many=True)
            return schema.dump(liste)
        
        except Exception as e:
            print('getFaqList hata',str(e))
            return False