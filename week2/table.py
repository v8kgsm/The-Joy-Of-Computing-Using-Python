# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:52:34 2020

@author: Vikas Tiwari
"""
b=True
while b:
    try:
        print("1-Start\n2-Exit\nEnter Your Choice:")
        n=int(input())
        if(n==1):
            try:
                print("*****TABLE*****")
                print("Enter a number of which table is to be printed:")
                t=int(input())
            except ValueError:
                print("Enter correct Value.")
                continue
            try:
                print("Enter a number till which you want table to be printed:")
                t1=int(input())
            except ValueError:
                print("Enter correct Value.")
                continue
            for i in range(0,t1+1,1):
                print(t,"*",i,"=",t*i)
        if(n==2):
            b=False
            exit  
    except ValueError:
        print("Enter correct Value.")
        continue
