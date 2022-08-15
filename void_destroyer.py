from websockets import connect
from placebotweb import *
from protocol import *
from headers import *
from canvas import *
from PIL import Image
import asyncio
import sys

im = Image.open("canvas.png").convert("RGB")
pixels = im.load()
width, height = im.size

delay = 0.135

pos = (0, 508)
size = (501, 516)

void_rect = (pos[0], pos[1], size[0], size[1])

def inside_rect(pos, rect):
	x1, y1, w, h = rect
	x2, y2 = x1 + w, y1 + h
	x, y = pos
	
	if x1 < x and x < x2:
		if y1 < y and y < y2:
			return True
	
	return False

async def bot(uri):
	print("Starting bot...")

	async with connect(uri, extra_headers=headers) as websocket:
		canvas_im = get_canvas()
		canvas_pixels = canvas_im.load()

		for y in range(1024):
			for x in range(1024):
				if canvas_pixels[x, y] != pixels[x, y] and inside_rect((x, y), void_rect) and (canvas_pixels[x, y] == (0, 0, 0) or canvas_pixels[x, y] == (36, 80, 164)):
					print("Updating " + str(x) + ", " + str(y))

					canvas_pixels[x, y] = pixels[x, y]

					if canvas_pixels[x, y] == (36, 80, 164):
						canvas_pixels[x, y] = (255, 255, 255)

					await websocket.send(encode_pixel(x, y, canvas_pixels[x, y]))

					packet_data = await websocket.recv()

					if len(packet_data) == 11:
						decoded_data = decode_pixel(packet_data)
						canvas_pixels[decoded_data["x"], decoded_data["y"]] = decoded_data["color"]

					await asyncio.sleep(delay)

		print("Finished!")
		sys.exit()

asyncio.run(bot("wss://pl.g7kk.com/ws"))