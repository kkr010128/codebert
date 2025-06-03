import networkx as nx
n, m = map(int, input().split())
nodes = [0 for i in range(n)]
L = []
for i in range(m):
    a, b = map(int, input().split())
    L.append((a,b))
    nodes[a-1] += 1
    nodes[b-1] += 1

num = 0

for node in nodes:
    if node == 0:
        num += 1

graph = nx.from_edgelist(L)
num += len(list(nx.connected_components(graph)))

print(num-1)