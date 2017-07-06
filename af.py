#!/usr/bin/env python

import random
from PIL import Image, ImageFont, ImageDraw

fontSize = 28

#font = ImageFont.load_default().font
font = ImageFont.truetype("Flame.ttf", fontSize)

#im=Image.open("package.jpg")
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

#message = "Celebrate the 4th with..." + random.choice(elements) + " " + random.choice(animals)
message = random.choice(elements) + " " + random.choice(animals)

# TODO: Center text on box
draw.text((10, 10), message, font=font)
im.show()
