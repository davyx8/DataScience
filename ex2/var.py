
import networkx as nx
import matplotlib.pyplot as plt

import numpy
import scipy.optimize
import random

    
edges = set()
nodes = set()
    
with open('fbegonet.txt') as fh:
    for edge in fh:
        x,y = edge.split()
        x,y = int(x),int(y)
        edges.add((x,y))
        edges.add((y,x))
        nodes.add(x)
        nodes.add(y)

print("number of edges: " + str(len(edges)))
print("number of nodes: " + str(len(nodes)))
    #print(nodes)

G = nx.Graph()
for e in edges:
  G.add_edge(e[0],e[1])
nx.draw(G)
plt.show()
plt.clf()

connectedComponents = list(nx.connected_components(G))
print(len(connectedComponents))
print(connectedComponents)
len(connectedComponents)
len(connectedComponents[0])

'''
    ### Find all 3 and 4-cliques in the graph ###
    cl3 = set()
    cl4 = set()
    for x in nodes:
        for y in nodes:
            if not ((x,y) in edges): continue
            for z in nodes:
                if not ((x,z) in edges): continue
                if not ((y,z) in edges): continue
                clique = [x,y,z]
                clique.sort()
                cl3.add(tuple(clique))
                for k in nodes:
                    if not ((x,k) in edges): continue
                    if not ((y,k) in edges): continue
                    if not ((z,k) in edges): continue
                    clique = [x,y,z,k]
                    clique.sort()
                    cl4.add(tuple(clique))
                    
    
    #Clique Percolation
    communities = set()
    result_communities = set()
    done = False
    for cliques in cl4:
        communities.add(cliques)
        result_communities.add(cliques)
    
    print("Clique Percolation")
    #passctr = 0
    while not done:
        #passctr = passctr + 1
        #if passctr % 50 == 0:
        #    print("Passctr: " + str(passctr))
        #    print("result_community: " + str(len(result_communities)))
        
        done = True
        pass1 = False
        for community1 in result_communities:
            for community2 in result_communities:
                I = set(community1)
                J = set(community2)
                for c3 in cl3:
                    c3s = set(c3)
                    if community1 is not community2 and c3s.issubset(I) and c3s.issubset(J):
                        done = False
                        result_communities.remove(community1)
                        result_communities.remove(community2)
                        newSet = I.union(J)
                        result_communities.add(tuple(newSet))
                        pass1 = True
                        done = False
                        break
                    
                if pass1: break;
            if pass1: break;
                    
    print("Total Communities: " + str(len(result_communities)))
    for t in result_communities:
        print("Community_len: " + str(len(t)))
        print("Nodes: \n" + str(t))
        '''
                    
''' 
    G = nx.Graph()
    for e in edges:
        G.add_edge(e[0], e[1])
    nx.draw(G)
    plt.show()
    plt.clf()
'''
    
tp1()