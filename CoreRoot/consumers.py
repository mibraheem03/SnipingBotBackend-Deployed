import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from Client_Data import new_client_into_df

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print("New Bot Trying to Connect To Server")
        self.accept()

   
    def disconnect(self, code):
        print("User Left" + str(code))


    def receive(self, text_data):
        print("Message Recieved From Client")
        bot_information = json.loads(text_data)
        print(bot_information)
        #Information From Client
        '''
            "ip": external_ip,
            "profit": profit,
            'IP_Address': external_ip,
            'Client_ID': 'testingBot',
            'Status': 'Running',
            'Profit': profit,
            'Comission': '0',
            'DateStared': datetime.datetime.now(),
            'TradedVolume': '0',
        '''
        new_client_into_df(bot_information)
