from helpers.sqlServer import SqlConnect

class Register:
    def __init__(self):
        self.sql = SqlConnect().data
        
    def setRegister(self,data):
        try:
            self.sql.update_insert("""
                                        insert into MekmarCom_Musteriler(adi,kullaniciadi,mailadres,telefon) values(?,?,?,?)
                                   
                                   
                                   """,(data['name'],data['username'],data['email'],data['phone']))
            return True
        
        except  Exception as e:
            print('setRegister hata',str(e))
            return False