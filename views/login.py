from helpers.sqlServer import SqlConnect

class Login:
    def __init__(self):
        self.sql = SqlConnect().data
    
    def getLogin(self,username):
        try:
            result = self.sql.getStoreList("""
                                                select * from MekmarCom_Musteriler where kullaniciadi=?
                                           
                                           """,username)
            if(len(result)>0):
                return True
            else:
                return False
        
        except Exception as e:
            print('getLogin hata',str(e))
            return False