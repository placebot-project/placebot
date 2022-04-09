const ws = require('ws');

function putUint32(b: any, offset: number, n: number) {
	let view = new DataView(b);
	view.setUint32(offset, n, false);
}

function getUint32(b: any, offset: number) {
	let view = new DataView(b);
	return view.getUint32(offset, false);
}

function encodePixel(x: number, y: number, color: any) {
	let b = new Uint8Array(11);

	putUint32(b.buffer, 0, x);
	putUint32(b.buffer, 4, y);

	for (let i = 0; i < 3; i++) {
		b[8 + i] = color[i];
	}

	return b;
}

function decodePixel(data: ArrayBuffer) {
	console.log(data);

	return {
		x: getUint32(data, 0),
		y: getUint32(data, 4),
		color: new Uint8Array(data.slice(8))
	};
}

class Place {
	hostname: string
	socket: any
	https: boolean
	pixelCallback: any

	constructor(hostname: string, https: boolean, pixelCallback: any) {
		this.hostname = hostname;
		this.https = https;
		this.pixelCallback = pixelCallback;
		this.socket = new ws(`${this.https ? "wss://" : "ws://"}${hostname}/ws`);
		
		this.socket.on("message", data => {
			if (data.length == 11) {
				console.log(data);
				this.pixelCallback(decodePixel(data.buffer));
			}
		});
	}

	placePixel(x: number, y: number, color: Uint8Array) {
		this.socket.send(encodePixel(x, y, color));
	}
}

module.exports = {
	Place
};