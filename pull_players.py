import requests
import json
import unicodedata


def pull():
    url = "https://fifa23.content.easports.com/fifa/fltOnlineAssets/23DF3AC5-9539-438B-8414-146FAFDE3FF2/2023/fut/items/web/players.json"

    resp = requests.get(url=url)
    pretty_response = json.loads(unicodedata.normalize('NFKD', resp.text).encode('ascii', 'ignore'))
    json_players = json.dumps(pretty_response, indent=4)
    with open("./json_data/players.json",'w') as players_json:
        players_json.write(json_players)
