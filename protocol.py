# This makes no sense, but this is how the pl/ace protocol works

import struct

def encode_pixel(x, y, color):
	encoded_x = x.to_bytes(4, "big")
	encoded_y = y.to_bytes(4, "big")

	encoded_color = bytes([color[0], color[1], color[2]])

	return encoded_x + encoded_y + encoded_color

def decode_pixel(data):
	data_array = bytearray(data)

	return {
		"x": struct.unpack("!I", bytes([data[0]]) + bytes([data[1]]) + bytes([data[2]]) + bytes([data[3]]))[0],
		"y": struct.unpack("!I", bytes([data[4]]) + bytes([data[5]]) + bytes([data[6]]) + bytes([data[7]]))[0],
		"color": (data_array[8], data_array[9], data_array[10])
	}