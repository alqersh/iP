print('''
 __  ____     __  _____ _____ ___
 |  \/  \ \   / / |_   _|  __ \__ \
 | \  / |\ \_/ /    | | | |__) | ) |
 | |\/| | \   /     | | |  ___/ / /
 | |  | |  | |     _| |_| |    |_|
 |_|  |_|  |_|    |_____|_|    (_)
                     by IG:@127.1.0.0.1
''')
import requests
import json
ip=requests.get("https://api.ipify.org/?format=json").json()['ip']
print('your ip:'+ip)
