import json

import pandas as pd

Clients = pd.DataFrame(columns=['IP_ADDRESS', 'CLIENT_ID', 'PROFIT', 'COMMISSION'])

#row = {
#    "IP_ADDRESS": "TEST",
#    "CLIENT_ID": "TEST",
#    "PROFIT": "0",
#    "COMMISSION": "0"
#}


def new_client(IP, ID):
    row = {
        'IP_ADDRESS': IP,
        'CLIENT_ID': ID,
        'PROFIT': 'NA',
        'COMMISSION': 'NA'
    }
    Clients.insert(row)


def update_client(IP, ID, PROFIT, COMMISSION):
    for index, client in Clients.iterrows():
        if client['ID'] == ID:
            client['IP'] = IP
            client['PROFIT'] = PROFIT
            client['COMMISSION'] = COMMISSION


def make_json():
    json_information = []
    for index, client in Clients.iterrows():
        var = {
            "IP_ADDRESS": client["IP_ADDRESS"][index],
            "CLIENT_ID": client["CLIENT_ID"][index],
            "PROFIT": client["PROFIT"][index],
            "COMMISSION": client["COMMISSION"][index]
        }
        json_information.push(var)
    #json.dump(json_information)
    return json_information
