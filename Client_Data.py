import json

import pandas as pd
from threading import Lock, Thread
import datetime

Clients = pd.DataFrame(columns=['IP_Address', 'Client_ID','Status', 'Profit', 'Comission', 'TradedVolume', 'DateStared'])


def new_client_into_df( IP, ID):
        global Clients
        row = {
            'IP_Address': IP,
            'Client_ID': ID,
            'Status':'Running',
            'Profit': '0',
            'Comission': '0',
            'DateStared': datetime.datetime.now(),
            'TradedVolume': '0',
            'Profit':'0'
        }
        Clients = Clients.append(row,ignore_index=True)
        print(Clients.to_string())


def update_client(IP, ID, PROFIT, COMMISSION):
    for index, client in Clients.iterrows():
        if client['ID'] == ID:
            client['IP'] = IP
            client['PROFIT'] = PROFIT
            client['COMMISSION'] = COMMISSION


def make_json():
    json_information = []

    print(Clients.to_string())
    for index, client in Clients.iterrows():
       var = {
           "IP_Address": client["IP_Address"],
           "Client_ID": client["Client_ID"],
           'Status': client['Status'],
           "Comission": client["Comission"],
           'DateStared': client['DateStared'],
           'TradedVolume': client['TradedVolume'],
           'Profit': client['Profit']
       }
       json_information.append(var)
    #json.dump(json_information)
    return json_information
