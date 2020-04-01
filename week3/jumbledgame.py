# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:50:28 2020

@author: user
"""
import random

def choose():
    words=['rainbow','computer','science','programing','mathematics','player','condition','reverse','water','board']
    pick=random.choice(words)
    return pick

def jumble(word):
    j="".join(random.sample(word,len(word)))
    return j

def thank(p1n,p2n,pp1,pp2):
    print(p1n," Your score is", pp1)
    print(p2n," Your score is", pp2)
    print("Thank You Visit Again.")
    
def play():
    p1name=input("Enter player1 name:")
    p2name=input("Enter player2 name:")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computers task
        picked_word=choose()
        #create question
        qn=jumble(picked_word)
        print(qn)
        #for player 1
        if(turn%2==0):
            print(p1name," your turn")
            ans=input("what is on my mind?")
            if(ans==picked_word):
                pp1=pp1+1
                print("Your score:",pp1)
            else:
                print("Better luck next time!!,I thought ",picked_word)
            c=int(input("Press 1 to continue or Press 0 to exit?"))
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break
        #for player 2
        else:
            print(p2name," your turn")
            ans=input("what is on my mind?")
            if(ans==picked_word):
                pp2=pp2+1
                print("Your score:",pp2)
            else:
                print("Better luck next time!!,I thought ",picked_word)
            c=input("Press 1 to continue or Press 0 to exit.")
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break 
        turn=turn+1
play()