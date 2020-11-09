#! /usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import sys

im = Image.open('canvas.bmp')

draw = ImageDraw.Draw(im)
font = ImageFont.load("./fonts/scientifica-11.pil")
draw.text((10,10), "hello world", font=font, fill = 128)
font = ImageFont.load("./fonts/curieMedium-12.pil")
draw.text((10,20), "hello world", font=font, fill=128)
font = ImageFont.load("./fonts/curieBold-12.pil")
draw.text((10,30), "hello world", font=font, fill=128)

# write to stdout
im.show()

im.save('draw.png')
