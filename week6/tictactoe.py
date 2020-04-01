# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:26:52 2020

@author: user
"""

import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s="X"
p2s="O"

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if(board[r][c]==symbol):
                count+=1
        if(count==3):
            print(symbol," has Won")
            return True
    return False

def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if(board[r][c]==symbol):
                count+=1
        if(count==3):
            print(symbol," has Won")
            return True
    return False

def check_diag(symbol):
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol):
        print(symbol," has Won")
        return True
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol):
        print(symbol," has Won")
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diag(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter your row position(1/2/3):"))
        column=int(input("Enter your column position(1/2/3):"))
        if(row>0 and row<4 and column>0 and column<4 and board[row-1][column-1]=='-'):
            break
        else:
            print("Invalid Input Provided.")
        board[row-1][column-1]=symbol
        


def play():
    for turn in range(9):   #for 9 cells in the matrix  
        if(turn%2==0):
            print("X-P1-Turn")
            place(p1s)
            if(won(p1s)):
                break
        else:
            print("O-P2-Turn")
            place(p2s)
            if(won(p2s)):
                break
            
    if not (won(p1s)) and not(won(p2s)):
        print("Draw")   

play()
            