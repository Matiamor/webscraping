from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/6.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

url = 'https://www.amazon.es/s?k=tarjeta+grafica&i=computers&rh=n%3A667049031%2Cp_36%3A1323857031&s=review-rank&dc&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=95HP1H4872EX&qid=1645126858&rnid=1323854031&sprefix=tarjeta+grafica%2Caps%2C87&ref=sr_st_review-rank'
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

#Nombre tarjeta grafica

tg = soup.find_all('span', class_="a-size-medium a-color-base a-text-normal")

tarjetas = list()

count = 0

for i in tg:
      if count < 10:     
           tarjetas.append(i.text)
      else:
            break
      count = count + 1



#Valoracion

vl = soup.find_all('span', class_="a-icon-alt")

valoracion = list()

count = 0

for i in vl:
      if count < 10:
            valoracion.append(i.text)
      else:
            break
      count = count + 1



#Precio

pr = soup.find_all('span', class_="a-price-whole")

precios = list()

count = 0

for i in pr:

      if count < 10:
            precios.append(i.text)
      else:
            break
      count = count + 1



#Caracteristicas

tr = soup.find_all('div', class_="sg-col sg-col-0-of-12 sg-col-4-of-16 sg-col-2-of-20 s-padding-right-small")

car = list()
carac = list()
count = 1

for i in tr:
      if count < 42:                    
            t = i.find('span', class_= "a-text-bold")
            car.append(t.text) 
      else:
            break
      count = count + 1

for f in range(10):
    carac.append([0]*4)
aux = 0
for t in range(10):
    for c in range(4):
        carac[t][c] = car[aux]
        aux = aux + 1
    

archivo = open("Tarjetas.txt","w")
for i in range(10):
    archivo.write( "NOMBRE: " + tarjetas[i]+'\n'+ "VALORACION: "+valoracion[i] + '\n' +"PRECIO EN EUROS: " + precios[i] + '\n')
    archivo.write( "Tamaño de RAM   " +  "Tipo de RAM   " + "Tarjeta grafica   " + "Velocidad de memoria   " + '\n')
    for j in range(4):
            archivo.write(carac[i][j] + "    ")
    archivo.write('\n'+ '\n' + '\n')        
    

archivo.close()
