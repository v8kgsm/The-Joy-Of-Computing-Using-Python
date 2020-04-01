# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:50:03 2020

@author: user
"""
#importing mean from the statistics package
from statistics import mean

Estimates=[122,312,443,43,144,299,876,544,334,55,32,353,232,23,654,300,455,100,130,104]
#print(len(Estimates))
#sorted by default in asscending order using sort function
print("Unsorted:",Estimates)
Estimates.sort()
#Trimed Value = tv
print("Sorted:",Estimates)
#for calculating trimed mean
# we removed 10% smaller and largest data from the total data set 

tv=int(0.1*len(Estimates))   #calculation of trimed value
#int will take the floor value

print("Trimed value:",tv)
# Removing 10% of smaller value using slicing 
Estimates=Estimates[tv:]
print("Slicing smaller 10%:",Estimates)
# Removing 10% of largest value using slicing
Estimates=Estimates[:(len(Estimates)-tv)]
print("Slicing 10% of largest data:",Estimates)
#calculating mean value of the trimed data set
print("Mean:",mean(Estimates))
