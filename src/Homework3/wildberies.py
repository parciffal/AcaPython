import requests
import json
from pprint import pprint


get_all_categoryes_with_sub_categories = "https://static.wbstatic.net/data/main-menu-ru-ru-v2.json"

re = requests.get(get_all_categoryes_with_sub_categories)
data = re.json()
pprint(data)


get_info = "https://catalog.wb.ru/catalog/{shard}/catalog?appType=1&cat={query}&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&lang=ru&locale=ru&pricemarginCoeff=1.0&reg=0&regions=80,64,83,4,38,33,70,68,69,86,75,30,40,48,1,66,31,22,71&sort=popular&spp=0"\
           .format("pants", "cat=8127")