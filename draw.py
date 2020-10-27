#! /usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
import sys

im = Image.open('canvas.bmp')

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

draw = ImageDraw.Draw(im)
font = ImageFont.load("./fonts/scientifica-11.pil")
draw.text((10,10), "hello world", font=font, fill=128)
font = ImageFont.load("./fonts/curieMedium-12.pil")
draw.text((10,20), "hello world", font=font, fill=128)
font = ImageFont.load("./fonts/curieBold-12.pil")
draw.text((10,30), "hello world", font=font, fill=128)
font = ImageFont.load("./fonts/curieItalic-12.pil")
draw.text((10,50), "hello world", font=font, fill=128)

# write to stdout
im.show()

im.save('draw.bmp')
