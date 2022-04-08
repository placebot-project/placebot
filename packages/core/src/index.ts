function putUint32(b, offset, n) {
	let view = new DataView(b);
	view.setUint32(offset, n, false);
}

function encodePixel(x, y, color) {
	let b = new Uint8Array(11);

	putUint32(b.buffer, 0, x);
	putUint32(b.buffer, 4, y);

	for (let i = 0; i < 3; i++) {
		b[8 + i] = color[i];
	}

	return b;
}

module.exports = {
	encodePixel
};