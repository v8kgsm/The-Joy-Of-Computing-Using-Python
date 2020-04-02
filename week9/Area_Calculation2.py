# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 08:51:48 2020

@author: Vikas Tiwari
"""

#you have to take RGB values and dimensions according to your pc values either it will throw error after running


from PIL import Image
import random
im=Image.open('areacal.png')
rgb_im=im.convert('RGB')    #conversion to matrix
count_in=0
count_pun=0
count=0
while(count<=10000):
    x=random.randint(0,424)
    y=random.randint(0,393)
    z=0
    r,g,b=rgb_im.getpixel((x,y))    #    corresponding to x and y it will RGB values
    if(r==60):
        count_in+=1
        count+=1
    else:
        if(r==80):
            count_pun+=1
            count+=1
            
area_pun=(count_pun/count_in)*3287263   #3287263 area of india   
print(area_pun)   