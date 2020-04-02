# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:34:36 2020

@author: user
"""
#ginifab.com
from PIL import Image
im=Image.open('test1.png')
rgb_im=im.convert("RGB")
r,g,b=rgb_im.getpixel((1,1))
print("Orange Color:",r,g,b)
r,g,b=rgb_im.getpixel((150,1))
print("Blue Color:",r,g,b)