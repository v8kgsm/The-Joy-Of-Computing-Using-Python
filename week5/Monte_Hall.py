# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:55:28 2020

@author: user
"""
import random
doors=[0]*3
goatsdoor=[0]*22
swap=0
dont_swap=0
j=0
while(j<10):
    x=random.randint(0,2)   #xth door will comprise of bmw
    doors[x]="BMW"
    for i in range( 0,3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
            goatsdoor.append(i)
    choice=int(input("Enter your choice:"))
    door_open=random.choice(goatsdoor)  #open a door that comprises of goat
    while(door_open==choice):   #door_open should not be equal to choice therefore ask again when it is same
        door_open=random.choice(goatsdoor)
    ch=input("Do You want to swap(y/n)?:")
    if(ch=="y"):
        if(doors[choice]=='Goat'):
            print("Player Wins")
            swap+=1
        else:
            print("Player Lost")
    else:
        if(doors[choice]=='Goat'):
            print("Player Lost")
        else:
            print("Player wins")
            dont_swap+=1
            
    j+=1
print("Swap Wins:",swap)
print("Don't Swap Wins:",dont_swap)

        

    