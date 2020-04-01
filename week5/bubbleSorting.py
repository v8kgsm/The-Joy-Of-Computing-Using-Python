# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 00:41:42 2020

@author: user
"""

def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                r=a[j]
                a[j]=a[j+1]
                a[j+1]=r
            
a=[1,3,6,2,5,9,4]
bubble(a)
for i in a:
    print(i,end=" ")
                