# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 13:25:17 2021

@author: Vladimir
"""



import requests
import json
import pprint

#мои репозитории 
r = requests.get('https://api.github.com/user/repos', auth=('qwertistuff', 'ключ удалил'))

#pp = pprint.PrettyPrinter(width=41, compact=True)
#pp.pprint(r.json())

#вся выдача
with open('data.json', 'w') as f:
    json.dump(r.json(), f)
    
    
#репозитории
with open('repos.txt', 'w') as f:
    for repos in r.json():
        f.write(repos['clone_url']+ '\n')
       # json.dump(repos['clone_url'], f)


