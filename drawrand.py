#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import time
import random

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from luma.core.render import canvas

SPEED=0.1

def create_device():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial,
                     cascaded=2,
                     block_orientation=90,
                     rotate=2)
    return device

def random_points(dev):
    with canvas(dev) as draw:
        draw.point((random.randint(0,15), random.randint(0,7)), fill="white")    
        draw.point((random.randint(0,15), random.randint(0,7)), fill="white")    

def main_loop(dev):
    try:
        while True:
            random_points(dev)
            #time.sleep(SPEED)    
    except KeyboardInterrupt:
        print('Bye')
    
if __name__ == "__main__":
    dev = create_device()
    main_loop(dev)
    dev.cleanup()
    
