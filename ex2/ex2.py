import numpy
import urllib
import scipy.optimize
import random
from sklearn.decomposition import PCA
from collections import defaultdict

### Network visualization ###
import networkx as nx
import matplotlib.pyplot as plt


edges = set()
nodes = set()
for e in urllib.urlopen("fbegonet.txt"):
  x,y = e.split()
  x = int(x)
  y = int(y)
  edges.add((x,y))
  edges.add((y,x))
  nodes.add(x)
  nodes.add(y)


G = nx.Graph()
for e in edges:
  G.add_edge(e[0],e[1])
nx.draw(G)
plt.show()
plt.clf()
G2 = nx.Graph()


connectedComponents = list(nx.connected_components(G))

for gr in connectedComponents:
  print(len(gr))
print(len(connectedComponents[0]))
w=len(connectedComponents[0])
print(len(connectedComponents))

print(connectedComponents[0])
sortedarr=sorted(connectedComponents[0])


def splitter(A):
    B = A[0:len(A)//2]
    C = A[len(A)//2:]

    return (B,C)

B,C=splitter(sortedarr)

def norm_cut(B,C,edges):
  cut=0
  volB=0
  volC=0
  for e in edges:
    x,y = e[0],e[1]
    x = int(x)
    y = int(y)
    if( (x in  connectedComponents[0])  and (y in connectedComponents[0] )):
      G2.add_edge(e[0],e[1])
      if ((x in B) and (y in C)):
        cut=cut+1
      if ((y in B)):
        volB=volB+1
      if ((x in C)):
        volC=volC+1
  return (float(cut)/volB+float(cut)/volC)


nx.draw(G2)
plt.show()
plt.clf()
print('the initial normalized cut is: ')
print(norm_cut(B,C,edges))




import networkx as nx
import numpy as np
import logging


'''

cliques3 = set()
cliques4 = set()
for n1 in nodes:
  for n2 in nodes:
    if not ((n1,n2) in edges): continue
    for n3 in nodes:
      if not ((n1,n3) in edges): continue
      if not ((n2,n3) in edges): continue
      clique = [n1,n2,n3]
      clique.sort()
      cliques3.add(tuple(clique))
      for n4 in nodes:
        if not ((n1,n4) in edges): continue
        if not ((n2,n4) in edges): continue
        if not ((n3,n4) in edges): continue
        clique = [n1,n2,n3,n4]
        clique.sort()
        cliques4.add(tuple(clique))

c = list(nx.k_clique_communities(G,4))
print(len(c))
print(len(c[0]))
''' 