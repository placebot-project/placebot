from websockets import connect
from protocol import *
from headers import *
from PIL import Image
import asyncio
import time
import sys

im = Image.open(sys.argv[1])
pixels = im.load()
width, height = im.size

offset = ((1024 // 2) - (width // 2), (1024 // 2) - (height // 2))

async def bot(uri):
	async with connect(uri, extra_headers=headers) as websocket:
		for y in range(height):
			for x in range(width):
				color = pixels[x, y]

				await websocket.send(encode_pixel(offset[0] + x, offset[1] + y, (color[0], color[1], color[2])))
				await websocket.recv()
				time.sleep(0.3)

asyncio.run(bot("wss://pl.g7kk.com/ws"))