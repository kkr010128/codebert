import networkx as nx
N, M = map(int, input().split())

G = nx.Graph()

G.add_edges_from(tuple(map(int, input().split())) for _ in range(M))

dist = nx.shortest_path_length(G, target=1)
print('Yes')
for i in range(2, N+1):
  print(min((dist[j], j) for j in nx.all_neighbors(G, i))[1])
    



