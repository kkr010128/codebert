n = int(input())
G = [[0]]+[list(map(int, input().split()))[2:] for _ in range(n)]
# print(G)
from collections import deque
d = deque([1])
dist  = [10**10 for _ in range(n+1)]
dist[1] = 0
while len(d) != 0:
    now = d.popleft()
    # print(now)
    for nexte in G[now]:
        if dist[now] +1 < dist[nexte]:
            dist[nexte] = dist[now] + 1
            d.append(nexte)
for i,d in enumerate(dist[1:]):
    if d != 10**10:
        print(i+1,d)
    else:
        print(i+1,-1)

        

