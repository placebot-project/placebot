from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests
import zipfile
import json
import os

def download_web_zip():
	response = requests.get("https://github.com/thatretrodev/placebot-web/releases/download/0.0.1/dist.zip")

	f = open("dist.zip", "wb")
	f.seek(0)
	f.write(response.content)
	f.close()

def start_server(image, x, y, config_checker):
	if not os.path.isdir("web"):
		print("Downloading a static build of placebot-web...")
		
		download_web_zip()

		os.mkdir("web")

		with zipfile.ZipFile("dist.zip", "r") as f:
			f.extractall("web")
		
		os.remove("dist.zip")
	
	# TODO: Make the static files work!
	app = Flask("Placebot", static_folder="web", static_url_path="/")

	CORS(app)

	@app.route("/api/status", methods=["GET"])
	def api_status():
		configured = config_checker()

		if configured:
			return jsonify({
				"configured": True,
				"image": image,
				"x": x,
				"y": y
			})
		else:
			return jsonify({
				"configured": False
			})
	
	app.run(port=8090)

#if __name__ == '__main__':
#	app.run()