from PIL import Image
import pickle

def read_heatmap():
	f = open("heat.pickle", "rb")
	data = pickle.loads(f.read())
	f.close()
	return data

heat = read_heatmap()

print(heat)

im = Image.new("RGB", (1024, 1024), color=(0, 0, 0))
pixels = im.load()

for i in heat.keys():
	x = i[0]
	y = i[1]

	color = heat[i] * 50

	if color > 255:
		color = 255

	pixels[x, y] = (color, 0, 0)

im.save("output.png")