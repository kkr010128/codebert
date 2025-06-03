from networkx import *

n,m = map(int, input().split())
G = Graph()

for i in range(m):
    a,b = map(int, input().split())
    G.add_edges_from([(a, b)])

m3 = list(connected_components(G))

count = 0

if len(max(connected_components(G), key=len)) == n:
    print(0)
    exit()
else:
    for i in m3:
        count += len(i)

sub = n - count

if sub != 0:
    print((len(m3)-1)+sub)

else:
    print(len(m3)+sub-1)


