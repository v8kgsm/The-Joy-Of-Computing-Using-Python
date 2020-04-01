# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:50:50 2020

@author: user
"""
def fizzbuzz():
    n=int(input("Enter a number:"))
    for i in range(1,n+1,1):
        if(i%3==0 and i%5!=0):
            print(i,"= Fizz")
        elif(i%5==0 and i%3!=0):
            print(i,"= Buzz")
        elif(i%3==0 and i%5==0):
            print(i,"= FizzBuzz")
        else:
            print(i)

fizzbuzz()