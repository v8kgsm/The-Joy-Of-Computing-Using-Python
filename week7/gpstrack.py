# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:00:30 2020

@author: user
"""

import csv
from gmplot import gmplot
gmap = gmplot.GoogleMapPlotter(28.454532,77.443476,17)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"
with open("gps.csv","r") as f:
    #variable name reader
    reader=csv.reader(f)
    k=0
    #it will create iterator through the file named as f
    for row in reader:
        #lattitude
        lat=float(row[0])
        #longitude
        long=float(row[1])
        
        if(k==0):
            gmap.marker(lat ,long, 'yellow')
            k=1
        else:
            gmap.marker(lat ,long, 'blue')
    
gmap.marker(lat ,long, 'red')
gmap.draw("mymap.html")