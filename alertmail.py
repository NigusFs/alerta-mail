#python 2.7.14
from email.mime.text import MIMEText
import smtplib


def sendd(msg,price,dif):
	from_addr = 'automsgbot24@gmail.com'
	to_addr  = 'nicolas.floress@mail.udp.cl'
	msg = "{}, ${}, vario ${}".format(msg,price,dif)
 
	mime_msg=MIMEText(msg,"plain") #indica que el texto sea plano
	#mime_message = MIMEText(message, "plain", _charset="utf-8")

	mime_msg["From"]=from_addr 
	mime_msg["To"]=to_addr
	mime_msg["Subject"]="Mensaje automatico, cambio de precio en Ripley" #asunto
 
	server = smtplib.SMTP("smtp.gmail.com")
	server.starttls()
	server.login(from_addr,"1122334455_1")
	server.sendmail(from_addr, to_addr, mime_msg.as_string())
	server.quit()
#sendd("ps4",122)

