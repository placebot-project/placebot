import io
from PIL import Image
from headers import *
import requests
import json
import io

def get_canvas():
	response = requests.get("https://pl.g7kk.com/place.png", headers=headers)#"http://localhost:3000/place.png")

	if response.status_code != 200:
		return Image.new("RGB", (1024, 1024), color=(255, 255, 255))
	
	return Image.open(io.BytesIO(response.content))