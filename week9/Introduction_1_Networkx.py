# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 19:06:35 2020

@author: Vikas Tiwari
"""

""" For More Such Graphs visit blog of networkx """
import networkx as nx
import matplotlib.pyplot as plt

g   = nx.Graph()

''' one more way to add nodes if you want to add it in bulk
just follow following...
-->l=[1,2,3]
-->g.add_nodes_from()
and now you skip steps of adding each node indvidually
'''
    
''' one more way to plot it 
import networkx as nx
import matplotlib.pyplot as plt
G=nx.complete_graph(10)
nx.draw(G)
plt.show()

'''
''' 
Random Graph
import networkx as nx
import matplotlib.pyplot as plt
g=nx.gnp_random_graph(20,0.5))
nx.draw(g)
plt.show()
---> g=nx.gnp_random_graph(20,0.5)
'''

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,3)
print(g.nodes())

nx.draw(g)
plt.show()
