from websockets import connect
from protocol import *
from headers import *
from canvas import *
from PIL import Image
import asyncio
import time
import sys

im = Image.open(sys.argv[1]).convert("RGB")
pixels = im.load()
width, height = im.size

offset = ((1024 // 2) - (width // 2), (1024 // 2) - (height // 2))

async def bot(uri):
	async with connect(uri, extra_headers=headers) as websocket:
		canvas_im = get_canvas()
		canvas_pixels = canvas_im.load()

		y_startpos = int(sys.argv[3])

		for _y in range(height - y_startpos):
			for x in range(width):
				y = _y + y_startpos
				color = pixels[x, y]

				#print(canvas_pixels[offset[0] + x, offset[1] + y])
				#print(pixels[x, y])

				if canvas_pixels[offset[0] + x, offset[1] + y] != pixels[x, y]:
					#print(x, y)
					await websocket.send(encode_pixel(offset[0] + x, offset[1] + y, (color[0], color[1], color[2])))

					packet_data = await websocket.recv()

					if len(packet_data) == 11:
						decoded_data = decode_pixel(packet_data)

						print("Updating " + str(decoded_data["x"]) + ", " + str(decoded_data["x"]))
						canvas_pixels[decoded_data["x"], decoded_data["y"]] = decoded_data["color"]

					time.sleep(0.3)

asyncio.run(bot(sys.argv[2]))##"ws://localhost:3000/ws"))