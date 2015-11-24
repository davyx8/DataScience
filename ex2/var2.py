
import networkx as nx
import matplotlib.pyplot as plt

def tp1():
    
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

    #print("E: " + str(len(edges)))
    #print("N: " + str(len(nodes)))
    #print(nodes)
    
    ### Find all 3 and 4-cliques in the graph ###
    print("Getting cliques3/4")
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
                    
    
    #Clique Percolation
    communities = set()
    result_communities = set()
    done = False
    for cliques in cliques4:
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
                    
    print("Total Communities: " + str(len(result_communities)))
    for t in result_communities:
        print("Community_len: " + str(len(t)))
        print("Nodes: \n" + str(t))
        
                    
''' 
    G = nx.Graph()
    for e in edges:
        G.add_edge(e[0], e[1])
    nx.draw(G)
    plt.show()
    plt.clf()
'''
    
tp1()