import requests
import json

pid = 388
url = 'https://viri.tech/fut23/search.php'

payload = {'player_id':pid}


x = requests.post(url=url, json=payload)


print(x.text)