import dotenv
import os
import requests
from requests import Request
import pandas
from typing import  Type

import json

dotenv.load_dotenv(dotenv.find_dotenv())
page = 1
app_key = os.getenv('app_key')
app_secret = os.getenv('app_secret')
baseUrl = 'https://app.omie.com.br/api/v1/'
call = "ListarDepartamentos"
route = "geral/departamentos/"


url = baseUrl+route
param = [
        {
            "pagina": page,
            "registros_por_pagina": 50
        }
    ]
params = {
    "call": "{}".format(call),
    "app_key": "{}".format(app_key),
    "app_secret": "{}".format(app_secret),
    "param": param
}
data = []
page = 1

listAllDep = []
response = requests.post(url, json=params)

ret = response.json()
tp = int(ret['total_de_paginas'])
while page <= tp:

    
    res = requests.post(url, json=params)
    if res.status_code == 200:
        content = res.json()[list(response.json().keys())[-1]]
        data += list(content)
        page += 1
    else:
        print('Found {} pages from {} route!!'.format(page, call))
        break
    with open('filename.json', 'w') as json_file:
            json.dump(data, json_file)

