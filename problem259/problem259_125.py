import sys
input = sys.stdin.readline
from collections import *

def bfs(s):
    q = deque([s])
    dist = [-1]*N
    dist[s] = 0
    leaf = set()
    
    while q:
        v = q.popleft()
        flag = True
        
        for nv in G[v]:
            if dist[nv]==-1:
                dist[nv] = dist[v]+1
                q.append(nv)
                flag = False
                
        if flag:
            leaf.add(v)
    
    return dist, leaf

N, u, v = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(N-1):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

d1, _ = bfs(u-1)
d2, leaf = bfs(v-1)
ans = 0

for i in range(N):
    if i not in leaf and d1[i]<=d2[i]:
        ans = max(ans, d2[i])

print(ans)