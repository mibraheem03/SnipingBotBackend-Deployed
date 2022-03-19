import json

import pandas as pd
from threading import Lock, Thread


Clients = pd.DataFrame(columns=['IP_ADDRESS', 'CLIENT_ID', 'PROFIT', 'COMMISSION'])
class Client_Information():


    def new_client_into_df( IP, ID):
        global Clients
        row = {
            'IP_ADDRESS': IP,
            'CLIENT_ID': ID,
            'PROFIT': 'NA',
            'COMMISSION': 'NA'
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
           #var = {
           #    "IP_ADDRESS": client["IP_ADDRESS"][index],
           #    "CLIENT_ID": client["CLIENT_ID"][index],
           #    "PROFIT": client["PROFIT"][index],
           #    "COMMISSION": client["COMMISSION"][index]
           #}
            json_information.append({"IP" : "Test" ,
                                     "PROFIT" : "PROFIT"
                                     })
        #json.dump(json_information)
        return json_information
