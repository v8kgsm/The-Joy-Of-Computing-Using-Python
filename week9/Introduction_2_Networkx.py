# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:56:42 2020

@author: user
"""

import networkx as nx
import matplotlib.pyplot as plt
#g=nx.gnp_random_graph(20,0.3)
g=nx.barabasi_albert_graph(50,2)

nx.draw(g)
plt.show()

nx.write_gexf(g,"analysis.gexf")

'''
Gephi...Software
Print Number of nodes/edges/degrees.
print(g.nodes())
print(g.edges())
print(g.degree(0))
'''
























