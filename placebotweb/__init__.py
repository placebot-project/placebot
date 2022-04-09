from flask import Flask, jsonify
from flask_cors import CORS
import json

configured = False

def start_server(image, x, y):
	app = Flask("Placebot")

	CORS(app)

	@app.route("/api/status", methods=["GET"])
	def api_status():
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