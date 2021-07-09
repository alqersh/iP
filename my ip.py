import requests
import json
ip=requests.get("https://api.ipify.org/?format=json").json()['ip']
print('your ip:'+ip)