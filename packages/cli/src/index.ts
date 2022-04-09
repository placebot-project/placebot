const { Place } = require('@placebot/core');
const fs = require('fs');

const config = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));

if (process.argv.length == 4) {
	require('dotenv').config({ path: process.argv[3] });
}
else {
	require('dotenv').config();
}

if (require.main == module) {
	console.log(config);

	let place = new Place("localhost:3000", false, data => {console.log(data);});
	//console.log(protocol.encodePixel(0, 0, [255, 255, 255]));
}