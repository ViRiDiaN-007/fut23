import pull_club
import search_futbin
import pull_tradepile
import club_valuation
import pull_players
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while True:
    print('''

    [1]. Load players
    [2]. Get valuations 

    ''')
    ans = input("What would you like to do: ")
    cls()
    if int(ans)==1:
        while True:
            cls()
            print('''

                [1]. Get official EA Player list
                [2]. Pull club members
                [3]. Pull transfer list
                [4]. Refresh all
                [5]. Return to previous menu
            
            ''')
            ans = input("What would you like to do: ")
            if int(ans)==1:
                cls()
                print("Getting updated EA playerlist")
                pull_players.pull()
                cls()
                print('Players pulled and stored to ./json_data/players.json')
                print('Press any button to continue')
                input()
                cls()
                break
            elif int(ans)==2:
                cls()
                print("Getting list of your tradeable players. Depending on your club size, this could take a moment")
                pull_club.pull()
                print("Players pulled and stored to ./json_data/club_players.json")
                print("Press any button to exit")
                input()
                cls()
                break
            elif int(ans)==3:
                cls()
                print("Getting your transfer list")
                pull_tradepile.get_tradepile()
                print("Players pulled and stored to ./json_data/tradepile.json")
                print("Press any button to exit")
                input()
                cls()
                break
            elif int(ans)==4:
                cls()
                print("Getting updated EA playerlist")
                pull_players.pull()
                print('Players pulled and stored to ./json_data/players.json')
                print()
                print("Getting list of your tradeable players. Depending on your club size, this could take a moment")
                pull_club.pull()
                print("Players pulled and stored to ./json_data/club_players.json")
                print()
                print("Getting your transfer list")
                pull_tradepile.get_tradepile()
                print("Players pulled and stored to ./json_data/tradepile.json")
                print("Press any button to exit")
                input()
                cls()
                break
            elif int(ans)==5:
                cls()
                break
    
    elif int(ans) == 2:
        while True:
            cls()
            print('''

                    [1]. Get Club Valuation
                    [2]. Get Transfer List Profit/Loss
                    [3]. Return to previous menu
                
                ''')
            ans = input("What would you like to do: ")
            if int(ans)==1:
                cls()
                print("Getting Club Valuation. This could take a bit")
                club_valuation.get_club_valution()
                cls()
                print("Players pulled and stored to ./csv/club_list.csv")
                print("Press any button to exit")
                input()
                cls()
                break

            elif int(ans)==2:
                cls()
                print("Getting Transfer List Profit/Loss")
                club_valuation.trade_list_valuation()
                cls()
                print("Players Pulled and stored to ./csv/transfer_list.csv")
                print("Press any button to exit")
                input()
                cls()
                break
            elif int(ans)==3:
                cls()
                break



