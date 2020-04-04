# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:36:15 2020

@author: user
"""

#introduction of matrices with numpy

import numpy as np
x=np.array([[1,2],[3,4]],dtype=np.float64)
y=np.array([[5,6],[7,8]],dtype=np.float64)

print(x+y)
print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.sqrt(x,y))
print(np.square(x,y))

a=np.array([[1,2],[3,4]])
print(a)
print(a.T)  #transpose

print(np.sum(a))

print(np.sum(a,axis=0)) #sum of column