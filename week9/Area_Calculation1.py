# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:17:25 2020

@author: user
"""
#calculation of RGB value is possibel implicitly and explicitly

#you have to take RGB values and dimensions according to your pc values either it will throw error after running
import scipy.misc
import random

img=scipy.misc.imread('areacal.png')
count_pun=0     #for punjab
count_in=0      #for india
count=0
#more the number of iteration , more the accurate our answer will
         
"""
x is depth and y is length, in python it is reversed in case of images                                
x is horizontal value and y is vertical but in python  it is reversed
where x is vertical and y is horizontal
"""

while(count<=10000):
    x=random.randint(0,424)
    y=random.randint(0,393)     #dimension of the image is 393*424
    z=0
    if(img[x][y][z]==60):       # RGB value is calculated explicitly using online softwares
        count_in+=1
        count+=1
    else:
        if(img[x][y][z]==80):
            count_pun+=1
            count+=1
            
area_pun=(count_pun/count_in)*3287263   #3287263 area of india   
print(area_pun)



























