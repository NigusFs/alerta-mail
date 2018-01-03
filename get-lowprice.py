#python 2.7.14
from urllib import urlopen 
import re 
import sys
import alertmail

if __name__ == "__main__":

	
	##ps4
	precio_anterior=0
	archivo = open("precio_anterior.txt", "r")
	for linea in archivo.readlines():
		precio_anterior=int(linea)
	archivo.close() 

	url='https://simple.ripley.cl/consola-ps4-uncharted-4-thiefs-end-god-of-war-iii-remastered-horizon-zero-dawn-3-meses-suscripcion-premium-a-psn-2000365883353p'
	response = urlopen(url)
	html = response.read()
	html = html.decode('utf-8',"ignore")
	price=re.findall(r'"lowPrice" content="([0-9]*)"', html)#obtiene el precio
	price=int(price[0])

	if price < precio_anterior: #verifica si el precio es menor
		alertmail.sendd("Es momento de comprar el PlayStation",price, precio_anterior-price)
		archivo = open("precio_anterior.txt", "w")
		archivo.write(str(price))
		archivo.close()
		print("Correo enviado ps4 (-)")
	elif price > precio_anterior:
		alertmail.sendd("Subio el precio del PlayStation",price, price - precio_anterior)
		archivo = open("precio_anterior.txt", "w")
		archivo.write(str(price))
		archivo.close()
		print("Correo enviado ps4 (+)")
	else:
		print("nada")
	##joystick
	precio_anterior1=0
	archivo = open("precio_anterior1.txt", "r")
	for linea in archivo.readlines():
		precio_anterior1=int(linea)
	archivo.close()

	url1='https://simple.ripley.cl/control-sony-dualshock-4-jet-black-2000361188544p'
	response1 = urlopen(url1)
	html1 = response1.read()
	html1 = html1.decode('utf-8',"ignore")
	price1=re.findall(r'"lowPrice" content="([0-9]*)"', html1)
	price1=int(price1[0])


	if price1<precio_anterior1:
		alertmail.sendd("Es momento de comprar el Joystick",price1, precio_anterior1-price1)
		archivo = open("precio_anterior1.txt", "w")
		archivo.write(str(price1))
		archivo.close()
		print("Correo enviado joystick (-)") 
	elif price1>precio_anterior1:
		alertmail.sendd("Subio el precio del Joystick",price1, price1 - precio_anterior1)
		archivo = open("precio_anterior1.txt", "w")
		archivo.write(str(price1))
		archivo.close()
		print("Correo enviado joystick (+)") 
	else:
		print("nada")

