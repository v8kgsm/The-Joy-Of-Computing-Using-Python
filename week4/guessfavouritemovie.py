# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:11:24 2020

@author: user
"""
import random

def create_question(movie):
    n=len(movie)    
    letters=list(movie)
    temp=[]
    for i in range(n):
        if(letters[i]==' '):
            temp.append(' ')
        else:
            temp.append("*")
    qn=''.join(str(x) for x in temp)
    return qn
    
def is_present(letter,movie):
    c=movie.count(letter)
    if(c==0):
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if(ref[i]==' ' or ref[i]==letter):
            temp.append(ref[i])
        else:
            if(qn_list[i]=='*'):
                temp.append("*")
            else:
                temp.append(ref[i])
    qn1=''.join(str(x) for x in temp)
    return qn1   
    
movies=['anand','drishyam','nayakan','anbe sivam','gol maal','vikram vedha','black friday','dangal','manichithrathazhu','taare zameen par']
def play():
    p1name=input("Enter P1name:")
    p2name=input("Enter P2name:")
    pp1=0
    pp2=0
    turn=0
    b=True #as long as they willing to play they can play
    while b:
        if(turn%2==0):
            #player 1
            print(p1name," it's your turn.")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            Not_said=True
            while Not_said:
                letter=input("Your Guess:")
                if(is_present(letter,picked_movie)):
                   #unlock
                   modified_qn=unlock(modified_qn,picked_movie,letter)
                   print(modified_qn)
                   d=int(input("press 1 to guess the movie or 2 to unlock another letter as hint?"))
                   if(d==1):
                       ans=input("Your answer:")
                       if(ans==picked_movie):
                           pp1+=1
                           print("Correct Guess.")
                           Not_said=False
                           print(p1name,' your score is ',pp1)
                       else:
                            print("wrong answer, try again.")
                           
                else:
                    print(letter," not found.")
            c=int(input("Press 1 to continue or 0 to quit:"))
            if(c==0):
                print(p1name," your score:",pp1)
                print(p2name," your score:",pp2)
                print("Thanks for playing.")
                b=False
        else:
            #player 2
            print(p2name," it's your turn.")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            Not_said=True
            while Not_said:
                letter=input("Your Guess:")
                if(is_present(letter,picked_movie)):
                   #unlock
                   modified_qn=unlock(modified_qn,picked_movie,letter   )
                   print(modified_qn)
                   d=int(input("press 1 to guess the movie or 2 to unlock another letter as hint?"))
                   if(d==1):
                       ans=input("Your answer:")
                       if(ans==picked_movie):
                           pp2+=1
                           print("Correct Guess.")
                           Not_said=False
                           print(p2name,' your score is ',pp2)
                       else:
                            print("wrong answer, try again.")
                           
                else:
                    print(letter," not found.")
            c=int(input("Press 1 to continue or 0 to quit:"))
            if(c==0):
                print(p1name," your score:",pp1)
                print(p2name," your score:",pp2)
                print("Thanks for playing.")
                b=False
            
        
        turn=turn+1
                    
play()