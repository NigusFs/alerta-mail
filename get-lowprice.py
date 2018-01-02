#python 2.7.14
from urllib import urlopen 
import re 
import sys
import alertmail

if __name__ == "__main__":
	#url = 'https://knasta.cl/ripley/2000365883353p' #error al pasarlo a letras (decode con utf-8)
	##ps4

	url='https://simple.ripley.cl/consola-ps4-uncharted-4-thiefs-end-god-of-war-iii-remastered-horizon-zero-dawn-3-meses-suscripcion-premium-a-psn-2000365883353p'
	response = urlopen(url)
	html = response.read()
	html = html.decode('utf-8',"ignore")
	price=re.findall(r'"lowPrice" content="([0-9]*)"', html)#obtiene el precio

	##joystick
	url1='https://simple.ripley.cl/control-sony-dualshock-4-jet-black-2000361188544p'
	response1 = urlopen(url1)
	html1 = response1.read()
	html1 = html1.decode('utf-8',"ignore")
	price1=re.findall(r'"lowPrice" content="([0-9]*)"', html1)

	if int(price[0]) < 269991: #verifica si el precio es menor
		alertmail.sendd("PlayStation",price[0])
		print("correo enviado ps4")
	if int(price1[0])<49991:
		alertmail.sendd("Joystick",price1[0])
		print("correo enviado joystick")  


