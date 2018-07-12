from urllib.request import urlopen

import pandas as pd
import matplotlib as plt
import json
import googlemaps
from datetime import datetime


df = pd.read_csv('/Users/andreameroplaza/Documents/AnalisisExploratorioDeDatos/PrimerParcial/Exploratorio/ProyectoAED/USA/boston_bigdata.csv')
companies = df['company'].tolist()
company_search_name = []
s = '+'



#solo dos nombres de la compañía
for company in companies:
    temp = company.strip().split(' ')
    line = s.join(temp[0:2])
    company_search_name.append(line)


url_part1 = 'https://maps.googleapis.com/maps/api/geocode/json?address='
url_part2 = '&components=administrative_area:MA|country:US' #contry and state
lista_url = []

for company in company_search_name:
    lista_url.append(url_part1 + company + url_part2)

print(lista_url)

list_lat = []
list_lng =  []
gmaps = googlemaps.Client(key='AIzaSyCcCJL5M739cb5bDvcQDRwtZ5nUI4O8LVU')



for url in lista_url:
    try:
        jsonurl = urlopen(url)
        text = json.loads(jsonurl.read())
        for str in text['results']:
            print(str['geometry']['location']['lat'])
            print(str['geometry']['location']['lng'])
            list_lat.append(str['geometry']['location']['lat'])
            list_lng.append(str['geometry']['location']['lng'])
    except ValueError:
        print("Error")


df['Latitude'] = list_lat
df['Longitude'] = list_lng








