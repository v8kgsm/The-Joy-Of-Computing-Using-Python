# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 20:55:12 2020

@author: user
"""
a=[12,12,32,546,32,1,6,4,24,6,24,35,22,5,35,445,3,42,13,3,23,2,24,13,43,5,5,45,45,2]
print("Enter a range of number to be added in the list:",end='')
n=int(input())
for i in range(n):
    n1=int(input("Enter a number:"))
    a.append(n1)
print("Enter a number to find the frequency of the number from the list:")
t=int(input())
print("The number", t,"is repeated  repeated",a.count(t),"times")
print("List:",a)