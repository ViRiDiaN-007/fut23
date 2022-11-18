import requests
import search_futbin
import json
import unicodedata
import csv

def get_master_player_list():
    url = 'https://fifa23.content.easports.com/fifa/fltOnlineAssets/23DF3AC5-9539-438B-8414-146FAFDE3FF2/2023/fut/items/web/players.json'
    players = requests.get(url)
    return json.loads(unicodedata.normalize('NFKD', players.text).encode('ascii', 'ignore'))

def get_fifa_player_info(player_id, player_list):
    for player in player_list['Players']:
        if int(player_id)==int(player['id']):
            first_name = player['f']
            lastname = player['l']
            return first_name, lastname

def get_club_valution():
    header = ['first_name', 'last_name', 'rating', 'purchase_price', 'current_price', 'profit_on_trade']

    master_player_list = get_master_player_list()
    valuation = 0
    errors = 0
    with open('./json_data/club_players.json','r')as club_players, open('./csv/club_list.csv', 'w')as club_file:
        writer = csv.writer(club_file)
        writer.writerow(header)
        json_club_players = json.load(club_players)
        for player in json_club_players['itemData']:
            if 'loans' in player:
                continue
            if player['untradeable']==True:
                continue
            player_id = player['assetId']
            rating = player['rating']
            purchase_price = player['lastSalePrice']
        # print(player_id)
            #Get FIFA information on the player
            first_name, last_name =  get_fifa_player_info(player_id, master_player_list)
            if ' ' in first_name:
                first_name = first_name.split(' ')[1]

            #Search player nane on futin to convert to their player id
            futbin_id = search_futbin.search_by_name(first_name, player_id, rating)
            if futbin_id == None:
                print(f"Player not found. Retrying search with {first_name} {last_name}")
                futbin_id = search_futbin.search_by_name(f'{first_name} {last_name}', player_id, rating)
                if futbin_id == None:
                    print(f"Player still not found. Retrying search with {last_name}")
                    futbin_id = search_futbin.search_by_name(f'{last_name}', player_id, rating)
                    if futbin_id == None:
                        print('Shit out of luck brother')
                        errors +=1
                        continue

            futbin_player_blob = search_futbin.search_player(futbin_id)

            current_price = search_futbin.get_current_price(futbin_player_blob, futbin_id)
            valuation += int(current_price)
            #print(f'Value of player {player_id} is: {current_price}')
            data = [first_name, last_name, rating, purchase_price, current_price, int(current_price)-int(purchase_price)]
            writer.writerow(data)
            club_file.flush()
            print(f'Player ID: {player_id}\t|\tPlayer Value: {current_price}\t|\tClub Valuation: {valuation}')

    print(valuation)
    print("Errors: ", errors)


def trade_list_valuation():
    header = ['first_name', 'last_name', 'rating', 'purchase_price', 'current_price', 'profit_on_trade']
    valuation = 0
    profit = 0
    cost = 0
    master_player_list = get_master_player_list()
    with open('./json_data/tradepile.json','r')as tradepile, open('./csv/transfer_list.csv', 'w')as transfer_file:
        writer = csv.writer(transfer_file)
        writer.writerow(header)
        json_tradepile = json.load(tradepile)
        for player in json_tradepile['auctionInfo']:
            player_id = player['itemData']['assetId']
            purchase_price = player['itemData']['lastSalePrice']
            rating = player['itemData']['rating']

            #Grab EA information on player for Futbin pricing lookup
            first_name, last_name =  get_fifa_player_info(player_id, master_player_list)
            if ' ' in first_name:
                first_name = first_name.split(' ')[1]

            #Search player nane on futbin to convert to their player id
            futbin_id = search_futbin.search_by_name(first_name, player_id, rating)
            if futbin_id == None:
                print(f"Player not found. Retrying search with {first_name} {last_name}")
                futbin_id = search_futbin.search_by_name(f'{first_name} {last_name}', player_id, rating)
                if futbin_id == None:
                    print(f"Player still not found. Retrying search with {last_name}")
                    futbin_id = search_futbin.search_by_name(f'{last_name}', player_id, rating)
                    if futbin_id == None:
                        print('Shit out of luck brother')
                        errors +=1
                        continue

            futbin_player_blob = search_futbin.search_player(futbin_id)
            current_price = search_futbin.get_current_price(futbin_player_blob, futbin_id)
            valuation +=current_price
            profit += current_price-purchase_price
            prof_on_trade = current_price - purchase_price
            cost += purchase_price
            data = [first_name, last_name, rating, purchase_price, current_price, prof_on_trade]
            writer.writerow(data)
            transfer_file.flush()
            print(f'Player Name: {first_name} {last_name}\t|\tPurchase Price: {purchase_price}\t|\tCurrent Price: {current_price}\t|\tProfit on Trade: {current_price-purchase_price}\t|\tTotal Profit/Loss: {profit}')