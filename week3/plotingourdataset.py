# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:44:05 2020

@author: user
"""
import statistics
import matplotlib.pyplot as p
#from scipy import stats 
Estimates=[122,312,443,43,144,299,876,544,334,55,32,353,232,23,654,300,455,100,130,104]
#y is taken as a constant
y=[]
#5    
Estimates.sort()
#m = stats.trim_mean(Estimates,0.1)
tv=int(0.1*len(Estimates))
Estimates=Estimates[tv:]
Estimates=Estimates[:(len(Estimates)-tv)]
# appending values
for i in range(len(Estimates)):
    y.append(5)
#ploting the grapgh for data set
p.plot(Estimates,y,'r--'    ) #predicted value by crowd computing

#mean of the data set
p.plot([statistics.mean(Estimates)],[5],'ro')

#median for the dataset
p.plot([statistics.median(Estimates)],[5],'bs')

#ploting the graph for actual value
p.plot([300],[5],'g^')

