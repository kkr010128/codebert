# -*- coding: utf-8 -*-

from collections import deque

################ DANGER ################
test = ""
#test = \
"""
9 6 1
1 2
2 3
3 4
4 5
5 6
4 7
7 8
8 9
ans 5
"""

"""
5 4 1
1 2
2 3
3 4
3 5
ans 2
"""

"""
5 4 5
1 2
1 3
1 4
1 5
ans 1
"""
########################################
test = list(reversed(test.strip().splitlines()))
if test:
    def input2():
        return test.pop()
else:
    def input2():
        return input()
########################################  
        
n, taka, aoki = map(int, input2().split())

edges = [0] * (n-1)
for i in range(n-1):
    edges[i] = tuple(map(int, input2().split()))

adjacencyL = [[] for i in range(n+1)]
for edge in edges:
    adjacencyL[edge[0]].append(edge[1])
    adjacencyL[edge[1]].append(edge[0])    

################ DANGER ################
#print("taka", taka, "aoki", aoki)
#import matplotlib.pyplot as plt
#import networkx as nx
#G = nx.DiGraph()
#G.add_edges_from(edges)
#nx.draw_networkx(G)
#plt.show()
########################################

takaL = [None] * (n+1)
aokiL = [None] * (n+1)
takaL[taka] = 0
aokiL[aoki] = 0
takaQ = deque([taka])
aokiQ = deque([aoki])

for L, Q in ((takaL, takaQ), (aokiL, aokiQ)):
    while Q:
        popN = Q.popleft()
        for a in adjacencyL[popN]:
            if L[a] == None:
                Q.append(a)
                L[a] = L[popN] + 1
                
    #print(L)
    
print(max(aokiL[i] for i in range(1, n+1) if takaL[i] < aokiL[i]) - 1)
