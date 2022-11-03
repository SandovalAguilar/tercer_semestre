'''
file -- table_to_dataframe.py -- 
'''

#Liberias necesarias
import requests 
from bs4 import BeautifulSoup as bs
import json
import re
import pandas as pd

#Clases
class website: 

    site_name = "Mis Profesores"
    def __init__(self, apartado, URL):
        self.section = apartado
        self.URL = URL

#Programa principal
def to_dataframe():

    URL_site = "https://www.misprofesores.com/escuelas/UANL-FCFM_2263"
    site = website("table", URL_site)
    
    html = requests.get(site.URL, verify = True)
    soup = bs(html.content, "html.parser")

    raw_json = raw_json = soup.find_all('script', type = 'text/javascript')
    str_json = "[" + re.search(r'{"i.*":\s*"(.*?)"}', str(raw_json)).group() + "]"
    str_to_json = json.loads(str_json)
    
    df = pd.json_normalize(str_to_json)


    return df


