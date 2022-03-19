from websocket_server import WebsocketServer
from log import log
import json
from Client_Data import Client_Information
info = Client_Information()
# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	log.info("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us")
	info.new_client_into_df("TEST", "TEST")


# Called for every client disconnecting
def client_left(client, server):
	log.info("Client(%d) disconnected" % client['id'])
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	log.info("client said: " + str(message))

	if len(message) > 200:
		message = message[:200]+'..'
	print("Client(%d) said: %s" % (client['id'], message))
	#update_client


PORT=7890
server = WebsocketServer(port = PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
#server.run_forever()