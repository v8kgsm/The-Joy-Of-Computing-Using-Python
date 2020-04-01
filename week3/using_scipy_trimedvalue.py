# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 11:26:27 2020

@author: user
"""

from scipy import stats
Estimates=[122,312,443,43,144,299,876,544,334,55,32,353,232,23,654,300,455,100,130,104]
Estimates.sort()
m = stats.trim_mean(Estimates,0.1)
print("Mean:",m)