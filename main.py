from websockets import connect
from placebotweb import *
from protocol import *
from headers import *
from canvas import *
from PIL import Image
import threading
import asyncio
import random
import time
import sys

def check_config():
	test_request = requests.get("https://pl.g7kk.com/stat", headers=headers)

	if test_request.status_code != 200:
		return False
	else:
		return True

def start_web_interface():
	pass
	#start_server(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), check_config)

im = Image.open(sys.argv[1]).convert("RGB")
pixels = im.load()
width, height = im.size

if width > 100 or height > 100:
	exit()

offset = (int(sys.argv[2]), int(sys.argv[3]))
#offset = (387, 381)
#offset = (620, 508)
#offset = (55, 68)
#offset = (114, 5)
# offset = ((1024 // 2) - (width // 2), (1024 // 2) - (height // 2))

delay = 0.125

if len(sys.argv) == 5:
	delay = float(sys.argv[4])

#if len(sys.argv)

async def bot(uri):
	print("Starting bot...")

	async with connect(uri, extra_headers=headers) as websocket:
		canvas_im = get_canvas()
		canvas_pixels = canvas_im.load()

		for y in range(height):
			for x in range(width):

				#print(x, y)

				#print(canvas_pixels[offset[0] + x, offset[1] + y])
				#print(pixels[x, y])
				
				color = pixels[x, y]

				if canvas_pixels[offset[0] + x, offset[1] + y] != pixels[x, y]:
					#print(x, y)
					print("Updating " + str(offset[0] + x) + ", " + str(offset[1] + y))
					await websocket.send(encode_pixel(offset[0] + x, offset[1] + y, (color[0], color[1], color[2])))

					packet_data = await websocket.recv()

					if len(packet_data) == 11:
						decoded_data = decode_pixel(packet_data)

						#print("Updating " + str(decoded_data["x"]) + ", " + str(decoded_data["x"]))
						canvas_pixels[decoded_data["x"], decoded_data["y"]] = decoded_data["color"]

					await asyncio.sleep(delay)
		print("Finished!")
		sys.exit()

#async def pixelwar(uri):
#	print("Starting bot...")
#
#	async with connect(uri, extra_headers=headers) as websocket:
#		while True:
#			packet_data = decode_pixel(await websocket.recv())
#			if packet_data["color"] == (0, 0, 0) or packet_data["color"] == (173, 21, 25) or packet_data["color"] == (250, 189, 0):
#				print(packet_data["x"], packet_data["y"])
#				await asyncio.sleep(delay)
#				await websocket.send(encode_pixel(packet_data["x"], packet_data["y"], (255, 255, 255)))
#				await asyncio.sleep(delay)

asyncio.run(bot("wss://pl.g7kk.com/ws"))