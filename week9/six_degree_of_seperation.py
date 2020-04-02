# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:48:41 2020

@author: user
"""

#download data from http://snap.stanford.edu/data/ego-Facebook.html

import networkx as nx
import numpy 
G=nx.read_edgelist("facebook_combined.txt")

N=list(G.nodes())

spll=[]     #shortest path linked list
for u in N:         #u is node
    for v in N:     #v is another node
        if(u!=v):
            l=nx.shortest_path_length(G,u,v)
            print("Shortest path between ",u," and", v," is of length ",l)
            spll.append(l)
            
min_spl=min(spll)
max_spl=max(spll)        
avg_spl=numpy.average(spll)

print("Minimum shortest path:",min_spl)
print("Maximum shortest path:",max_spl)
print("Average shortest path:",avg_spl)























