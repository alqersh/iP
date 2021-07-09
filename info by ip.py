  _____ _   _ ______ ____    ______     __  _____ _____
 |_   _| \ | |  ____/ __ \  |  _ \ \   / / |_   _|  __ \
   | | |  \| | |__ | |  | | | |_) \ \_/ /    | | | |__) |
   | | | . ` |  __|| |  | | |  _ < \   /     | | |  ___/
  _| |_| |\  | |   | |__| | | |_) | | |     _| |_| |
 |_____|_| \_|_|    \____/  |____/  |_|    |_____|_|
                                        BY IG:@127.1.0.0.1
import requests
import json
query = input('target ip:')
url = f'http://ip-api.com/json/{query}'
req = requests.get(url=url).text
print(req)
