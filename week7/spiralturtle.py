# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 01:41:11 2020

@author: user
"""
import turtle

turtle.bgcolor('black')
seurat = turtle.Turtle()

width = 5
height = 7
 
dot_distance=25
seurat.setpos(-250,250)

#simple matrix
def spiral(m,n):
    #m is no. of rows
    #n is no. of columns
    #a is matrix
    k=0
    l=0
    f=0
    seurat.color('white')
    ''' 
    k is index of rows 
    l is index of columns
    
    '''
    while(k<m and l<n):
        if(f==1):
            seurat.right(90)
        #printing the first row from the remaining row
        for i in range(l,n):
            seurat.forward(dot_distance)
#            print(a[k][i],end=' ')
        k+=1
        f=1
        
        seurat.right(90)
        #printing the last column from the remaining column
        for i in range(k,m):
#            print(a[i][n-1],end=' ')
            seurat.forward(dot_distance)
        n-=1
        seurat.right(90)
        
        if(k<m):
            #printing the last row from the remaining row
            for i in range(n-1,l-1,-1):
                seurat.forward(dot_distance)
#                print(a[m-1][i],end=' ')
            m-=1
        seurat.right(90)
        
        if(l<n):
            #printing the first column from remaining columns
            for i in range(m-1,k-1,-1):
#                print(a[i][l],end=' ')
                seurat.forward(dot_distance)
            l+=1
        
#a=[]
#count=1
#for i in range(4):
#    l=[]
#    for j in range(4):
#        l.append(count)
#        count+=1
#    a.append(l) 
        
spiral(20,20)
turtle.done()