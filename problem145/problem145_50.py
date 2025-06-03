N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

from collections import deque
def solve():
    prev = [-1]*N
    prev[0]='Yes'
    d = deque([(0,0)])
    while len(d):
        v,cnt = d.popleft()
        for u in edge[v]:
            if prev[u]==-1:
                prev[u]=v+1
                d.append((u,cnt+1))
    if -1 in prev:
        return ['No']
    return prev
print(*solve(),sep='\n')
