# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:11:08 2020

@author: user
"""

import turtle
from random import randint
turtle.bgcolor('black')
seurat = turtle.Turtle()

width = 5
height = 7
 
dot_distance=25

seurat.penup()
list_color=['white','yellow','brown','red','green','orange','pink','violet','grey','blue','cyan']
seurat.setpos(-250,250)
def spiral(m,n):
    #m is no. of rows
    #n is no. of columns
    #i is iterator
    k=0
    l=0
    f=0
#    seurat.color('white')
    ''' 
    k is index of rows 
    l is index of columns
    
    '''
    col=randint(0,10)
    seurat.color(list_color[col])
    
    while(k<m and l<n):
        if(f==1):
            seurat.right(90)
        #printing the first row from the remaining row
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
        k+=1
        f=1
        
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        #printing the last column from the remaining column
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
        n-=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        if(k<m):
            #printing the last row from the remaining row
            for i in range(n-1,(l-1),-1):
                seurat.dot()
                seurat.forward(dot_distance)
            m-=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        if(l<n):
            #printing the first column from remaining columns
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
            l+=1
        
spiral(20,20)
turtle.done()




