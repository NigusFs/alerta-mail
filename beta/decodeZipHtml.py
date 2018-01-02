#python 2.7
from urllib import urlopen 
import re 
import sys
import gzip
import StringIO
import ssl

context = ssl._create_unverified_context()
response = urlopen("https://knasta.cl/ripley/2000365883353p/consola-ps4-uncharted-4-thiefs-end-god-of-war-iii-remastered-horizon-zero-dawn-3-meses-suscripcion-premium-a-psn", context=context)
#ssl permite saltarse la verificacion, antes tiraba un erro de autentificacion

if response.info().get('Content-Encoding') == 'gzip':
    buf = StringIO.StringIO( response.read())
    gzip_f = gzip.GzipFile(fileobj=buf)
    html = gzip_f.read()
else:
    html = response.read()

#gzip permite descomprimir bites q se obtienen desde paginas
#antes no se podia decodear ya que habian bites mayores q 0x8b

html = html.decode("utf-8","replace")
price=re.findall(r'precio', html)#obtiene el precio
#la wea no funciona porq no obtiene todo el codigo de la pagina
print(html)
print(price)
