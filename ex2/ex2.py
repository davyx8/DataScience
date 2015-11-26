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


#q6
print("Q6")
print("number of nodes : "+str(len(nodes)))
print("number of edges : "+str(len(edges)))

cliques3 = set()
cliques4 = set()
#Q7
print("Q7")
print("finding 3 and 4 cliques")
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
                


communities = set()
result_communities = set()
done = False
for cliques in cliques4:
    communities.add(cliques)
    result_communities.add(cliques)


print("finding communities")
while not done:

    
    done = True
    pass1 = False
    for community1 in result_communities:
        for community2 in result_communities:
            I = set(community1)
            J = set(community2)
            for c3 in cliques3:
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
                
print("Number of communities: " + str(len(result_communities)))
for t in result_communities:
    print("nodes in the community: \n" + str(t))
 
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
G2=G.subgraph(sortedarr)
nx.draw(G2)

for e in edges:
  x,y = e[0],e[1]
  x = int(x)
  y = int(y)

  #if( (x in  B)  or (y in C )):
   # G2.add_edge(x,y)
  #  G2.add_edge(y,x)
    
def normalized_cut_cost(first, second, edges, largest_connected_component):
  edge_num = 0
  for n1 in first:
    for n2 in second:
      if not ((n1, n2) in edges): continue
      edge_num += 1
  degree_first = sum(list(largest_connected_component.degree(first).values()))
  degree_second = sum(list(largest_connected_component.degree(second).values()))
  #print degree_first, degree_second
  result = (float(edge_num) / float(degree_first) + float(edge_num) / float(degree_second)) / 2.0
  return result


nx.draw(G2)

print("Q8a")
plt.show()
plt.clf()
print('the initial normalized cut is: ')
print(normalized_cut_cost(B,C,G2.edges(),G2))
#print(G2.edges())
print(len(sortedarr))
print(len(nodes))

print("Q8b")
cnt=0
scores={}
while(True):
  scores={}
  cnt=cnt+1
  for i in B:
    B.remove(i)
    C.append(i)
    score=normalized_cut_cost(B,C,G2.edges(),G2)
    scores[i]=score
    C.remove(i)
    B.append(i)

  for i in C:
    C.remove(i)
    B.append(i)
    score=normalized_cut_cost(B,C,G2.edges(),G2)
    scores[i]=scores
    B.remove(i)
    C.append(i)
  key, value = max(scores.iteritems(), key=lambda x:x[1])
  if (value>maxscore):
    maxscore=value
  else:
    break
  if key in B:
    B.remove(key)
    C.append(key)
  if key in C:
    C.remove(i)
    B.append(i)

print('normalized cut after running:')
print(value)

