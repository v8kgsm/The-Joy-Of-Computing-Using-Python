# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:32:00 2020

@author: user
"""

def binary(l,x,start,end):
    #best case
    if(start==end):
        if(l[start]==x):
            return start
        else:
            return -1
    else:
        #divide it in to half just follow algorithm
        mid=int((start+end)/2)
        if(l[mid]==x):
            return x
        elif(l[mid]>x):
            return binary(l,x,start,mid-1)
        else:
            return binary(l,x,mid+1,end)
        
l=[]
print("Enter Number of Elements:")
n=int(input())
for i in range(1,n+1):
    print("Enter a value:")
    a1=int(input())
    l.append(a1)
l.sort()
print("Enter the key to be searched in the list:")
x=int(input())
s=binary(l,x,0,len(l)-1)
if(s==-1):
    print("Ohh Sorry!! Number not found.")
else:
    print("Number Found at", s," position.")