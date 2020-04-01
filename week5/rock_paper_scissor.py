# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:09:26 2020

@author: user
"""

def game(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num1[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Game Draw.")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("Player one Wins!!")
        
    elif(player_one[p1]=="Rock" and player_two[p2]=="Paper"):
        print("Player two Wins!!")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        print("Player one Wins!!")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissor"):
        print("Player two Wins!!")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Rock"):
        print("Player two Wins!!")
    elif(player_one[p1]=="Scissor" and player_two[p2]=="Paper"):
        print("Player one Wins!!")
        
player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Paper',1:'Rock',2:'Scissor'}
while(1):
    num1=input("Player one, Enter Your choice(Range of three numbers(eg:123)):")
    num2=input("Player Two, Enter Your choice(Range of three numbers(eg:123)):")
    bit1=int(input("Player one, Enter your secret:"))
    bit2=int(input("Player two, Enter your secret:"))
    game(num1,num2,bit1,bit2)
    ch=input("Do you want to continue(y/n)?")
    if(ch=='n'):
        break       
        