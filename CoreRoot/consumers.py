import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from Client_Data import new_client_into_df

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print("New Bot Trying to Connect To Server")
        self.accept()

   
    def disconnect(self, code):
        print("User Left")


    def receive(self, text_data):
        print("Message Recieved From Client")
        bot_information = json.loads(text_data)
        print(bot_information)
        new_client_into_df(bot_information['ip'], bot_information['botId'])
