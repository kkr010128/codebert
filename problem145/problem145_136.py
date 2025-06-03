#NEED RE-SOLVE LATER.
from collections import deque
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: x-1, map(int, input().split()))
    G[a].append(b)
    G[b].append(a)

q = deque([0])
visited = [None]+[-1]*(n-1)
while q:
    nx = q.pop()
    for g in G[nx]:
        if visited[g] != -1:
            continue
        visited[g] = nx
        q.appendleft(g)

print('Yes')
print(*[visit+1 for visit in visited[1:]], sep='\n')