from websockets import connect
from placebotweb import *
from protocol import *
from headers import *
from canvas import *
from PIL import Image
import platform
import asyncio
import time
import sys

def check_config():
	test_request = requests.get("https://pl.g7kk.com/stat", headers=headers)

	if test_request.status_code != 200:
		return False
	else:
		return True

if platform.system() == "Linux":
	print("Starting placebot-web...")
	
	placebot_web = PlacebotWeb()
	time.sleep(1)

	print("Updating status...")

	placebot_web.update_status(check_config(), sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

print("Loading image...")

im = Image.open(sys.argv[1]).convert("RGB")
pixels = im.load()
width, height = im.size

if width > 100 or height > 100:
	exit()

offset = (int(sys.argv[2]), int(sys.argv[3]))

delay = 0.125

if len(sys.argv) == 5:
	delay = float(sys.argv[4])

async def bot(uri):
	print("Starting bot...")

	async with connect(uri, extra_headers=headers) as websocket:
		canvas_im = get_canvas()
		canvas_pixels = canvas_im.load()

		for y in range(height):
			for x in range(width):
				color = pixels[x, y]

				if canvas_pixels[offset[0] + x, offset[1] + y] != pixels[x, y]:
					print("Updating " + str(offset[0] + x) + ", " + str(offset[1] + y))
					await websocket.send(encode_pixel(offset[0] + x, offset[1] + y, (color[0], color[1], color[2])))

					packet_data = await websocket.recv()

					if len(packet_data) == 11:
						decoded_data = decode_pixel(packet_data)
						canvas_pixels[decoded_data["x"], decoded_data["y"]] = decoded_data["color"]

					await asyncio.sleep(delay)
		print("Finished!")
		sys.exit()

asyncio.run(bot("wss://pl.g7kk.com/ws"))