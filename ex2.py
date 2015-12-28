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

len(edges)
len(nodes)

G = nx.Graph()
for e in edges:
  G.add_edge(e[0],e[1])
nx.draw(G)
plt.show()
plt.clf()

connectedComponents = list(nx.connected_components(G))
print(len(connectedComponents))
for gr in connectedComponents:
  print(len(gr))
print(len(connectedComponents[0]))


import networkx as nx
import numpy as np
import logging

def normalized_min_cut(graph):
    """Clusters graph nodes according to normalized minimum cut algorithm.
    All nodes must have at least 1 edge. Uses zero as decision boundary. 
    
    Parameters
    -----------
        graph: a networkx graph to cluster
        
    Returns
    -----------
        vector containing -1 or 1 for every node
    References
    ----------
        J. Shi and J. Malik, *Normalized Cuts and Image Segmentation*, 
        IEEE Transactions on Pattern Analysis and Machine Learning, vol. 22, pp. 888-905
    """
    m_adjacency = np.array(nx.to_numpy_matrix(graph))

    D = np.diag(np.sum(m_adjacency, 0))
    D_half_inv = np.diag(1.0 / np.sqrt(np.sum(m_adjacency, 0)))
    M = np.dot(D_half_inv, np.dot((D - m_adjacency), D_half_inv))

    (w, v) = np.linalg.eig(M)
    #find index of second smallest eigenvalue
    index = np.argsort(w)[1]

    v_partition = v[:, index]
    v_partition = np.sign(v_partition)
    return v_partition


if __name__ == "__main__":
    logging.basicConfig()

    #create graph
    #graph = nx.tutte_graph()
    graph = nx.barbell_graph(10, 0)
    #add some additional edges
    graph.add_edge(3, 13)
    graph.add_edge(4, 13)
    #graph = nx.lollipop_graph(10, 10)

    v_partition = normalized_min_cut(graph)
    colors = np.zeros((len(v_partition), 3)) + 1.0
    colors[:, 2] = np.where(v_partition >= 0, 1.0, 0)

    nx.draw(graph, node_color=colors)

'''
### Find all 3 and 4-cliques in the graph ###
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

# Given a clique size: 4
# Initialize every clique as it's own community - cliques4()

for x in cliques4:
	for y in cliques4:
		for z in cliques3:
			if (z in x and z in y):
				x1 = x + y
				y = y + x
				x = x1
'''
normalized_min_cut(connectedComponents[0])