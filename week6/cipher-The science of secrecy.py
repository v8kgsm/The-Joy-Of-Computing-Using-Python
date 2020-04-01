# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:11:56 2020

@author: user
"""

import string
dict={}
data=""
file=open("Outputofcipher.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-2]
print(dict)
with open("cipher_data.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print(data,end="")
file.close()    
