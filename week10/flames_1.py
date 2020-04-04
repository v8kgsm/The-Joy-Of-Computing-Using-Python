# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:02:04 2020

@author: Vikas Tiwari
"""

#josephus problem
#please watch how flames has been played then simulate it..

'''
FLAMES stands for/....
f=friends
L=love
A=affection
M=marriage
E=enemy
S=sister
'''

#Always repeat the count in anticlock wise manner to cancel the letters appropriately

#prerequisites
'''
import string
r='Viraj'
print(r.lower())
print(r.upper())
s=list(r)
print(s)
print(r.replace('V','*'))
print(r.replace('Vi','*'))
print(r.replace('Vi','*@'))
Note : It is case sensitive .
'''
'''
Slicing

l=['a','b','c','d','e','f','g']
print(l[1:])
print(l[:4])
print([:])
print(l.index['d'])
    
'''

#program follow up

import string

def remove_matching_letter(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if(l1[i]==l2[j]):
                c=l1[i]
                l1.remove(c)
                l2.remove(c)
                l=l1+['*']+l2
                return[l,True]
    l=l1+['*']+l2
    return[l,False]

p1=input("Enter  first name:")
p1=p1.lower()
p1=p1.replace(' ',' ')

p2=input("Enter second name:")
p2=p2.lower()
p2=p2.replace(' ',' ')

l1=list(p1)
l2=list(p2)
proceed=True
while proceed:
    ret_list=remove_matching_letter(l1,l2)
    con_list=ret_list[0]
    proceed=con_list[1]
    star_index=con_list.index('*')
    l1=con_list[:star_index]
    l2=con_list[star_index+1:]
    
count=len(l1)+len(l2)
result=['Friends','Love','Affection','Marriage','Enemy','Siblings']

while len(result)>1:
    split_index=(count%len(result))-1
    if(split_index>=0):
        right=result[split_index+1:]
        left=result[:split_index]
        result=right+left
    else:
        result=result[:len(result)-1]
print(result[0])


















