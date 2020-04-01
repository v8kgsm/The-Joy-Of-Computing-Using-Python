# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:04:22 2020

@author: user
"""
#Illustration of sorted function
#Example 1
#x=[3,5,2,4,1]
#print(sorted(x,reverse=True))
#[5, 4, 3, 2, 1]

#example 2
#x=['w','e','a','o','y','b','m']
#print(sorted(x))

##example 3
#x='python'
#print(sorted(x))

##exapmle 4
#x={'e':1,'r':5,'u':4,'h':0}
#print(sorted(x))
##sorting takes place with respect to keys

##Exapmle 5
#L=['ccccc','ddd','bbbbb','ee','aaaaaaa']
##sorting takes place according to the length of the string in the list
#print(sorted(L,key=len))

#Program for anagram
st1=input("Enter Your String:")
st2=input("Enter Your String:")
print(sorted(st1))
print(sorted(st2))
if(sorted(st1)==sorted(st2)):
    print("They are anagrams.")
else:
    print("They are not the anagrams.")













