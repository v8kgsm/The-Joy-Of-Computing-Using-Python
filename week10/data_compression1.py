# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:17:35 2020

@author: user
"""

# some functions of numpy

import numpy as np
a=np.array([1,2,3])
print(type(a))
print(a.shape)  #shape of array 
print(a[0],a[1],a[2])
print(a.dtype)  #data type of array

a3=np.array([1,2,3],dtype=np.int64)
print(a3)
print(a3.dtype)
a1=np.array([[1,2,3],[4,5,6]])
print(a1.shape) 

a2=np.zeros((2,2))
print(a2)

a2=np.ones((2,2))
print(a2)

c=np.full((2,2),6)
print(c)

d=np.random.random((2,2))
print(d)