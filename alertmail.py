#python 2.7.14
from email.mime.text import MIMEText
import smtplib


def sendd(obj,price):
	from_addr = 'msgbot@outlook.com'
	to_addr  = 'mail'
	msg = "Es momento de comprar {}, ${}".format(obj,price)
 
	mime_msg=MIMEText(msg,"plain") #indica que el texto sea plano
	#mime_message = MIMEText(message, "plain", _charset="utf-8")

	mime_msg["From"]=from_addr 
	mime_msg["To"]=to_addr
	mime_msg["Subject"]="Mensaje automatico, cambio de precio en knasta" #asunto
 
	server = smtplib.SMTP("smtp.live.com")
	server.starttls()
	server.login(from_addr,"pass")
	server.sendmail(from_addr, to_addr, mime_msg.as_string())
	server.quit()
#sendd(122)

