all: write_img.py
	Python write_img.py
	magick convert img.ppm img.png

 