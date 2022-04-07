from websockets import connect
from protocol import *
from headers import *
import asyncio
import pickle
import time

heatmap = {}

def update_heatmap():
	f = open("heat.pickle", "wb")
	f.seek(0)
	f.write(pickle.dumps(heatmap))
	f.close()

async def bot(uri, y):
	async with connect(uri, extra_headers=headers) as websocket:
		while True:
			packet_data = await websocket.recv()

			if len(packet_data) == 11:
				decoded_data = decode_pixel(packet_data)
				
				print(decoded_data)
			
				if not (decoded_data["x"], decoded_data["y"]) in heatmap:
					heatmap[(decoded_data["x"], decoded_data["y"])] = 0
				
				heatmap[(decoded_data["x"], decoded_data["y"])] += 1

				update_heatmap()

			time.sleep(0.1)

def create_bot(y):
	#asyncio.run(bot("ws://localhost:3000/ws", y))
	asyncio.run(bot("wss://pl.g7kk.com/ws", y))

create_bot(0)
