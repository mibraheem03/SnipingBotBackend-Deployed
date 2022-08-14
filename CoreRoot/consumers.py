import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from Client_Data import new_client_into_df, update_comission_address, update_comission_rate


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print("New Bot Trying to Connect To Server")
        async_to_sync(self.channel_layer.group_add)(
            'events',
            self.channel_name
        )
        self.accept()
        from Client_Data import comission_address, comission_rate
        self.send(text_data=json.dumps({'comission_address': comission_address, 'rate': comission_rate}))

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            'events',
            self.channel_name
        )
        print("User Left" + str(code))

    def receive(self, text_data):
        # print("Received event: {}".format(content))
        print("Message Recieved From Client")
        bot_information = json.loads(text_data)
        print(bot_information)
        # Information From Client
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

    def chat_message(self, event):
        # Handles the "chat.message" event when it's sent to us.
        print("HELLO")
        self.send(text_data=event["text"])

    async def send_message(self, event):
        # Send message to WebSocket
        print("IN SEND")
        await self.send(text_data={
            'type': 'alert',
            'details': 'An external API api.external.com needs some data from you'
        })

    def events_alarm(self, event):
        print("Sending Messages To Bot")
        update_comission_address(event['comission_address'])
        update_comission_rate(event['rate'])
        self.send(text_data=json.dumps(event))
