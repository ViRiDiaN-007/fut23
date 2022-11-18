import requests
import json
import yaml
import math


with open('./auth/config.yaml', 'r')as config_file:
    config = yaml.safe_load(config_file)

def get_tradepile():
    url = 'https://utas.mob.v1.fut.ea.com/ut/game/fifa23/tradepile'
    headers = {'Connection': 'keep-alive',
    'X-UT-SID': config['X-UT-SID'],
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br'}

    x = requests.get(url = url, headers=headers)

    if "expired session" in x.text:
        print("Auth information is invalid/expired. Please edit your auth cookies in ./auth/config.yaml")
        input()   
        exit()
        #print(x.text)
    with open('./json_data/tradepile.json','w')as players_file:
       players_file.write(x.text.strip('"').replace('\\"', '"'))