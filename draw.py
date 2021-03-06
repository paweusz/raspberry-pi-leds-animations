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

def box(device, i):
    #print i
    with canvas(device) as draw:
        draw.rectangle((i,i,15-i,7-i), outline="white", fill="black")    
    time.sleep(SPEED)

def rect(device):
    for i in range(0,3):
        box(device,i)
    for i in range(3,0,-1):
        box(device,i)

def rects(dev):
    for i in range(10):
        rect(dev)

def create_device():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial,
                     cascaded=2,
                     block_orientation=90,
                     rotate=2)
    return device

def point(dev, xy):
    with canvas(dev) as draw:
        draw.point(xy, fill="white")    
    time.sleep(SPEED)
   

def flying_point(dev):
    point(dev, (0,0))
    point(dev, (0,1))
    point(dev, (0,2))
    point(dev, (0,3))
    point(dev, (0,4))    
    point(dev, (0,5))
    point(dev, (0,6))
    point(dev, (0,7))    
    
    point(dev, (1,0))
    point(dev, (1,1))    
    point(dev, (1,2))
    point(dev, (1,3))
    point(dev, (1,4))
    point(dev, (1,5))
    point(dev, (1,6))
    point(dev, (1,7))    

    point(dev, (2,0))
    point(dev, (2,1))
    point(dev, (2,2))
    point(dev, (2,3))
    point(dev, (2,4))
    point(dev, (2,5))
    point(dev, (2,6))
    point(dev, (2,7))    

    point(dev, (3,0))
    point(dev, (3,1))    
    point(dev, (3,2))    
    point(dev, (3,3))
    point(dev, (3,4))
    point(dev, (3,5))
    point(dev, (3,6))
    point(dev, (3,7))

    point(dev, (4,0))
    point(dev, (4,1))    
    point(dev, (4,2))
    point(dev, (4,3))
    point(dev, (4,4))
    point(dev, (4,5))
    point(dev, (4,6))
    point(dev, (4,7))
    
    point(dev, (5,0))
    point(dev, (5,1))
    point(dev, (5,2))    
    point(dev, (5,3))
    point(dev, (5,4))
    point(dev, (5,5))
    point(dev, (5,6))
    point(dev, (5,7))
    
    point(dev, (6,0))
    point(dev, (6,1))
    point(dev, (6,2))
    point(dev, (6,3))    
    point(dev, (6,4))
    point(dev, (6,5))
    point(dev, (6,6))
    point(dev, (6,7))
    
    point(dev, (7,0))
    point(dev, (7,1))
    point(dev, (7,2))    
    point(dev, (7,3))
    point(dev, (7,4))
    point(dev, (7,5))
    point(dev, (7,6))
    point(dev, (7,7))
    
    point(dev, (8,0))
    point(dev, (8,1))
    point(dev, (8,2))
    point(dev, (8,3))    
    point(dev, (8,4))
    point(dev, (8,5))
    point(dev, (8,6))
    point(dev, (8,7))
    
    point(dev, (9,0))
    point(dev, (9,1))
    point(dev, (9,2))
    point(dev, (9,3))
    point(dev, (9,4))
    point(dev, (9,5))
    point(dev, (9,6))
    point(dev, (9,7))
    
    point(dev, (10,0))
    point(dev, (10,1))
    point(dev, (10,2))
    point(dev, (10,3))
    point(dev, (10,4))
    point(dev, (10,5))
    point(dev, (10,6))
    point(dev, (10,7))
    
    point(dev, (11,0))
    point(dev, (11,1))
    point(dev, (11,2))
    point(dev, (11,3))
    point(dev, (11,4))
    point(dev, (11,5))
    point(dev, (11,6))
    point(dev, (11,7))
    
    point(dev, (12,0))
    point(dev, (12,1))
    point(dev, (12,2))
    point(dev, (12,3))
    point(dev, (12,4))
    point(dev, (12,5))
    point(dev, (12,6))
    point(dev, (12,7))

    point(dev, (13,0))  
    point(dev, (13,1))
    point(dev, (13,2))
    point(dev, (13,3))
    point(dev, (13,4))
    point(dev, (13,5))
    point(dev, (13,6))
    point(dev, (13,7))   

    point(dev, (14,0))    
    point(dev, (14,1))
    point(dev, (14,2))
    point(dev, (14,3))
    point(dev, (14,4))
    point(dev, (14,5))
    point(dev, (14,6))
    point(dev, (14,7))

    point(dev, (15,0))
    point(dev, (15,1))
    point(dev, (15,2))
    point(dev, (15,3))
    point(dev, (15,4))
    point(dev, (15,5))
    point(dev, (15,6))
    point(dev, (15,7))
    
    
    
    
    
if __name__ == "__main__":
    dev = create_device()
    rects(dev)
    flying_point(dev)

    time.sleep(1)
    dev.cleanup()
    
