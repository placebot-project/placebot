const protocol = require('@placebot/core');

if (require.main == module) {
	console.log(protocol.encodePixel(0, 0, [255, 255, 255]));
}