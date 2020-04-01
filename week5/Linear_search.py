# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:45:52 2020

@author: user
"""

def Linear_search(n,x):

    element=[]
    for i in range(1,n):
        element.append(i)
    count=0
    flag=0
    for i in element:
        count+=1
        if(i==x):
            print("Number Found at:"+   str(i))
            flag=1
            break
        
    if(flag==0):
        print("Number is not found.")
    print("Number of Iteration:",count)
        
    
Linear_search(1001,50)