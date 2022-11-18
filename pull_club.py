import requests
import json
import yaml
import math
import os

with open('./auth/config.yaml', 'r')as config_file:
    config = yaml.safe_load(config_file)


player_count = int(config['playerCount'])
offset = 250

def GetPlayers(start):
    url = 'https://utas.mob.v1.fut.ea.com/ut/game/fifa23/club'

    headers = {'Connection': 'keep-alive',
    'X-UT-SID': config['X-UT-SID'],
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Content-Length': '69',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br'}
    payload = {"count":250, "sort":"desc", "sortBy": "value", "start":start, "type":"player"}

    x = requests.post(url = url, json = payload, headers=headers)

    if "expired session" in x.text:
        print("Auth information is invalid/expired. Please edit your auth cookies in ./auth/config.yaml")
        input()   
        exit()
        #print(x.text)
    with open('./json_data/club_players.json','a')as players_file:
       players_file.write(x.text.strip('"').replace('\\"', '"'))

def pull():
    start=0
    with open('./json_data/club_players.json','w')as players_file:
        pass
    for num in range(math.ceil(player_count/offset)):
        GetPlayers(start)
        start+=offset
    with open('./json_data/club_players.json','r')as original, open('./json_data/club_players.json_temp', 'w')as temp:
        text = original.read()
        altered = text.replace(']}{"itemData":[', ',')
        temp.write(altered)
    with open('./json_data/club_players.json','w')as original, open('./json_data/club_players.json_temp', 'r')as temp:
        text = temp.read()
        original.write(text)
    os.remove('./json_data/club_players.json_temp')
