from helpers.sqlServer import SqlConnect
from models.fabrication import *
import smtplib
from email.message import EmailMessage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask,request,jsonify

class SendMail:
    
    def __init__(self):
        self.data = SqlConnect().data
        
    def send(self):    
        try:
            mailBilgi = request.get_json()
            
            mail = smtplib.SMTP("mail.mekmar.com",587)          
            mail.ehlo()
            mail.starttls()

            # gmail kullanıcı adımı ve şifremi giriyorum.
            mail.login("site@mekmar.com", "Fer602759")  
            mesaj = MIMEMultipart()

            mesaj["From"] = "site@mekmar.com"        # Gönderen kişi
            mesaj["To"] = "bilgiislem@mekmar.com"          # Alıcı
            #mesaj['To'] = "bilgiislem@mekmar.com"
            

            mesaj["Subject"] = "Inquiry from www.mekmar.com"  # Konu

            body = f"""      
                            <table style="border:1px solid gray;">
                                <tr>
                                    <th style="border:1px solid gray;margin-right:5px;">Name</th>
                                    <th style="border:1px solid gray;margin-right:5px;">Email</th>
                                    <th style="border:1px solid gray;margin-right:5px;">Phone</th>
                                    <th style="border:1px solid gray;margin-right:5px;">Description</th>
                                    <th style="border:1px solid gray;">Gender</th>
                                    
                                </tr>
                                <tr>
                                    <td style="border:1px solid gray;margin-right:5px;">{mailBilgi['name']}</td>
                                    <td style="border:1px solid gray;margin-right:5px;">{mailBilgi['email']}</td>
                                    <td style="border:1px solid gray;margin-right:5px;">{mailBilgi['phone']}</td>
                                    <td style="border:1px solid gray;margin-right:5px;">{mailBilgi['description']}</td>
                                    <td style="border:1px solid gray;">{mailBilgi['gender']}</td>
                                </tr>
                            </table>
                           """

            body_text = MIMEText(body, "html")  
            mesaj.attach(body_text)
            mail.sendmail( mesaj["From"], mesaj["To"], mesaj.as_string())
                  
            return True
        except Exception as e:
            print("getFabricationList",str(e))
            return False
                
                
                