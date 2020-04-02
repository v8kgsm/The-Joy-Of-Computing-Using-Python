# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:19:48 2020

@author: user
"""

#estimation
#image consist of matrix of pixel
#RGB value of white : (255,255,255)
#RGB value of black : (0,0,0)

#creation of image

import numpy as np
from PIL import Image

width=5
height=4

array=np.zeros([height,width,3],dtype=np.uint8)     #3 represents the 3 bits of RGB
img=Image.fromarray(array)
img.save('test.png')

array1=np.zeros([100,200,3],dtype=np.uint8)
array1[:,:100]=[255,128,0]      #orange color
array1[:,100:]=[0,0,255]        #blue color
img=Image.fromarray(array1)
img.save('test1.png')


























