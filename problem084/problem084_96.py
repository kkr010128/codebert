import networkx as nx
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

G = nx.Graph()

n, m = map(int, readline().split())
if m == 0:
    print(1)
    sys.exit()
for i in range(m):
    a, b = map(int, readline().split())
    G.add_edge(a, b)

largest_cc = max(nx.connected_components(G), key=len)
print(len(largest_cc))

