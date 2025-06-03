import sys
input = sys.stdin.readline
from collections import *

def bfs():
    q = deque([0])
    pre = [-1]*N
    pre[0] = 0
    
    while q:
        v = q.popleft()
        
        for nv in G[v]:
            if pre[nv]==-1:
                pre[nv] = v
                q.append(nv)
    
    return pre

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

pre = bfs()
print('Yes')

for pre_i in pre[1:]:
    print(pre_i+1)