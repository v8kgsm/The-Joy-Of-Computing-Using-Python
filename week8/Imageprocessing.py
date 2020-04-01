# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:34:06 2020

@author: user
"""
#Example 1
#from PIL import Image
#img = Image.open("img1.png")
##images are processd in terms of matrices ie. transpose operation
#transpose_image=img.transpose(Image.FLIP_LEFT_RIGHT)
##save it to a human understandable format
#transpose_image.save("corrected.png")
#print("Done Processing(Flipping).")

#Example 2
import cv2
img = cv2.imread("img1.png")    #reading Image
clahe = cv2.createCLAHE()       #preparation for clahe
#this works well for black n white images.

#convert to grey scale image
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#apply enhancement
enh_img= clahe.apply(gray_img)

cv2.imwrite("enhanced.png",enh_img)     #saving it to proper format

print("Done Processing(Enhancement).")