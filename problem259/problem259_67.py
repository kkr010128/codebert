import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,u,v = LI()
Graph = [[] for i in range(N+1)]

for i in range(N-1):
    a,b = LI()
    Graph[a].append(b)
    Graph[b].append(a)

from collections import deque

q1 = deque([u])
distance1 = [-1]*(N+1)  # uから各頂点への最短距離
distance1[u] = 0

# bfs

while q1:
    n = q1.pop()
    for d in Graph[n]:
        if distance1[d] != -1:
            continue
        else:
            distance1[d] = distance1[n]+1
            q1.appendleft(d)

q2 = deque([v])
distance2 = [-1]*(N+1)  # vから各頂点への最短距離
distance2[v] = 0

# bfs

while q2:
    n = q2.pop()
    for d in Graph[n]:
        if distance2[d] != -1:
            continue
        else:
            distance2[d] = distance2[n]+1
            q2.appendleft(d)

q3 = deque([u])
distance3 = [-1]*(N+1)  # uから各頂点への最短距離、ただし青木君に追いつかれない
distance3[u] = 0

# bfs

while q3:
    n = q3.pop()
    for d in Graph[n]:
        if distance3[d] != -1 or distance1[d] >= distance2[d]:
            continue
        else:
            distance3[d] = distance3[n]+1
            q3.appendleft(d)

# 青木君に追いつかれずに行ける頂点まで行き、うろうろする

ans = max(distance2[i]-1 for i in range(1,N+1) if distance3[i] >= 0)

print(ans)