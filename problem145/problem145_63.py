import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
N,M = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(M)]
es = [[] for _ in range(N)]
for a,b in AB:
    a,b = a-1,b-1
    es[a].append(b)
    es[b].append(a)

prev = [-1] * N
visited = [0] * N
visited[0] = 1
from collections import deque
q = deque([0])
while q:
    v = q.popleft()
    for to in es[v]:
        if visited[to]: continue
        visited[to] = 1
        prev[to] = v
        q.append(to)

print('Yes')
for p in prev[1:]:
    print(p+1)