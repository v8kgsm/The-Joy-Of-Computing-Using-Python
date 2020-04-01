# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:34:41 2020

@author: user
"""

def binary_search(a,x):
    first_pos=0
    last_pos=len(a)-1
    flag=0
    count=0
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid=(first_pos+last_pos)//2
        if(x==a[mid]):
            flag=1
            print("The element is present at pos:"+str(mid))
            print("The number of iteration:",str(count))
            return 
        else:
            if(x<a[mid]):
                last_pos = mid-1
            else:
                first_pos = mid+1
    print("Number not found.")
a=[]
for i in range(1,10001):
    a.append(i)
    
binary_search(a,14)