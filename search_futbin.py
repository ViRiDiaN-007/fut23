import requests
import json



def search_player(player_id):
    url = f'https://futbin.org/futbin/api/23/fetchPlayerInformation?ID={player_id}&ap=1.0.1&platform=PC'
    headers = {'User-Agent':'Futbin/2 CFNetwork/1333.0.4 Darwin/21.5.0'}

    response = requests.get(url, headers=headers)

    #if 'notFound' in response.text:
    #    print(player_id)
   #     print(response.text)
    return response.text

def get_current_price(player_info, player_id):
    json_players = json.loads(player_info)['data']
    for player in json_players:
        if str(player_id)==str(player['ID']):
            current_price = player['LCPrice']
            return current_price

def search_by_name(player_name, player_id, rating):
    url = f'https://futbin.org/futbin/api/searchPlayersByName?playername={player_name}&year=23'
    headers = {'User-Agent':'Futbin/2 CFNetwork/1333.0.4 Darwin/21.5.0'}

    response = requests.get(url=url, headers=headers)
    
    for player in json.loads(response.text)['data']:
        if int(player['rating'])==int(rating) and str(player_id)==str(player['playerid']):
            return player['ID']


'''futbin_id = (search_by_name('gnabry', 206113, 85))

player_blob = search_player(futbin_id)
print(get_current_price(player_blob, futbin_id))'''