import json

import pandas as pd
from threading import Lock, Thread
import datetime
import traceback

Clients = pd.DataFrame(columns=['IP_Address', 'Client_ID','Status', 'Profit', 'Comission', 'TradedVolume', 'DateStared'])
def client_already_exist (client_Id):
    global Clients
    for index, client in Clients.iterrows():
        if(client['Client_ID'] == client_Id):
            return True
    return False
def remove_client (client_Id):
    global Clients
    for index, client in Clients.iterrows():
        if(client['Client_ID'] == client_Id):
            Clients.drop(index=index,inplace=True)


def new_client_into_df(new_bot_information):
    try:
        global Clients
        # SAMPLE new_bot_information
        '''
          "ip": external_ip,
          "profit": profit,
          'IP_Address': external_ip,
          'Client_ID': 'testingBot',
          'Status': 'Running',
          'Profit': profit,
          'Comission': '0',
          'DateStared': DATETIME,
          'TradedVolume': '0',
        '''
        row = {
            'IP_Address': new_bot_information['ip'],
            'Client_ID': new_bot_information['Client_ID'],
            'Status':'Running',
            'Profit': new_bot_information['Profit'],
            'Comission': new_bot_information['Comission'],
            'DateStared': new_bot_information['DateStarted'],
            'TradedVolume': new_bot_information['TradedVolume']
        }
        if client_already_exist(new_bot_information['Client_ID']):
            remove_client(new_bot_information['Client_ID'])
        Clients = Clients.append(row,ignore_index=True)
        print(Clients.to_string())
    except Exception as error:
        print('Exception  as {e}'.format(e=error))
        print(traceback.format_exc())


def update_client(IP, ID, PROFIT, COMMISSION):
    for index, client in Clients.iterrows():
        if client['ID'] == ID:
            client['IP'] = IP
            client['PROFIT'] = PROFIT
            client['COMMISSION'] = COMMISSION

#def update_status():
    #for index, client in Clients.iterrows():



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
