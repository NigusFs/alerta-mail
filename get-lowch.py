import requests
import alertmail

if __name__ == "__main__":

	##ps4
	header ={
		'Referer': 'https://knasta.cl/ripley/2000365883353p'
	}
	r=requests.get(
		'https://knasta.cl/api/products/view/ripley/2000365883353p?app_version=2.1.0', stream=True, headers=header)
	
	contenido =r.json()['prices']
	precio=contenido[-1]
	#print(precio.get('price'))
	precio=precio.get('price')
	
	##joystick
	header1 ={
		'Referer': 'https://knasta.cl/ripley/2000361188544p'
	}
	r1=requests.get(
		'https://knasta.cl/api/products/view/ripley/2000361188544p?app_version=2.1.0',stream=True, headers=header1)
	contenido =r1.json()['prices']
	precio1=contenido[-1]
	#print(precio1.get('price'))
	precio1=precio1.get('price')
	
	if int(precio) < 269990: #verifica si el precio es menor
		alertmail.sendd(" un PlayStation",int(precio))
		print("correo enviado ps4")
	if int(precio1)<49990:
		alertmail.sendd(" un Joystick",int(precio1))
		print("correo enviado joystick")  
	