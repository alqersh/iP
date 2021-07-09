import requests
import json
query = input('target ip:')
url = f'http://ip-api.com/json/{query}'
req = requests.get(url=url).text
print(req)