# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:37:13 2020

@author: user
"""

import csv
with open("gps.csv","r") as f:
    #variable name reader
    reader=csv.reader(f)
    #it will create iterator through the file named as f
    for row in reader:
        #lattitude
        lat=float(row[0])
        #longitude
        long=float(row[1])
        print(lat)
        print(long)
        print(lat+long)
        