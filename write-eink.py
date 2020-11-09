#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.dirname(os.path.realpath(__file__))
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
print(picdir)
print(libdir)
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd4in2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    epd = epd4in2.EPD()
    logging.info("init and Clear")
    epd.init()

    #display 4Gra bmp
    Himage = Image.open(os.path.join(picdir, 'draw.png'))
    epd.display_4Gray(epd.getbuffer_4Gray(Himage))
    time.sleep(4)

    logging.info("Goto Sleep...")
    epd.sleep()
    epd.Dev_exit()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd4in2.epdconfig.module_exit()
    exit()
