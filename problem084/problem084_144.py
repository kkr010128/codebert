from networkx import *
N,M = map(int,input().split())

if M==0:
  print(1)
  exit()
else:
  A = [list(map(int,input().split())) for m in range(M)]
  G = Graph()
  G.add_edges_from(A)
  print(len(max(connected_components(G),key=len)))