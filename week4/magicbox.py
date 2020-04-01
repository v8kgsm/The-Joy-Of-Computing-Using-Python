# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:12:48 2020

@author: vikas Tiwari
"""

def magicsquare(n):
    magicSquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
    i=n//2      #to take the floor value of the result.
    j=n-1
    num=n*n
    count=1
    while(count<=num):
        if(i==-1 and j==n):     #condition 4
            i=0
            j=n-2
        else:
            if(j==n):   #when column value is becoming equal to n
                j=0
            
            if(i<0):    #when row value is becoming equal to -1
                i=n-1
                
        if(magicSquare[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[i][j]=count
            count+=1
        #condition 1
        i=i-1
        j=j+1
        
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=' ')
        print()
    print("The sum of each row/column/diagonal is:",str(n*(n**2+1)/2))
        
def userinput():
    n=int(input("Enter the number:"))
    magicsquare(n)
    
userinput()