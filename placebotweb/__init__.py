import threading
import requests
import zipfile
import json
import os
import io

def download_web_dist():
	response = requests.get("https://github.com/thatretrodev/placebot-web/releases/download/0.0.2/dist.zip")

	os.mkdir("web")

	with zipfile.ZipFile(io.BytesIO(response.content), "r") as f:
		f.extractall("web")

def download_web_server():
	response = requests.get("https://github.com/thatretrodev/placebot-web/releases/download/0.0.2/placebot-server.zip")

	with zipfile.ZipFile(io.BytesIO(response.content), "r") as f:
		f.extract("placebot-web-linux-amd64")
		os.rename("placebot-web-linux-amd64", "placebot_web_do_not_run")
		os.system("chmod +x placebot_web_do_not_run")

class PlacebotWeb:
	def __init__(self):
		if not os.path.isdir("web"):
			print("Downloading a static build of the placebot-web client...")
			
			download_web_dist()
		
		if not os.path.isfile("placebot_web_do_not_run"):
			print("Downloading a static build of the placebot-web server...")
			
			download_web_server()
		
		threading.Thread(target=os.system, args=["./placebot_web_do_not_run web"]).start()
	def update_status(self, configured, image, x, y):
		payload = {
			"configured": configured,
			"image": image,
			"x": x,
			"y": y
		}

		requests.post("http://localhost:4000/api/setstatus", json=payload)