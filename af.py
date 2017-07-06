#!/usr/bin/env python


import random
import textwrap
from PIL import Image, ImageFont, ImageDraw

fontSize = 44

lineWidth = 15 # characters

#font = ImageFont.load_default().font
font = ImageFont.truetype("Flame.ttf", fontSize)

im=Image.open("explosion.jpg")
draw = ImageDraw.Draw(im)

animals_filename = "animals.txt"
elements_filename = "elements.txt"

with open(animals_filename) as animals_file:
	animals = animals_file.readlines()
animals = [x.strip() for x in animals]

with open(elements_filename) as elements_file:
	elements = elements_file.readlines()
elements = [x.strip() for x in elements]

message = random.choice(elements) + " " + random.choice(animals)

#txtw, txth = font.getsize(message)
#x = (im.width - txtw) / 2
#y = (im.height - txth) / 2
#draw.text((x, y), message, font=font)

para = textwrap.wrap(message, lineWidth)
w, h = font.getsize("foo")
msgHeight = h * len(para)
cur_h, pad = (im.height - msgHeight) / 2 , 10

for line in para:
	w, h = font.getsize(line)
	draw.text(((im.width - w) / 2, cur_h), line, font=font)
	cur_h += h + pad

im.show()
