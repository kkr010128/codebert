import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N,u,v = MI()
Graph = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b = MI()
    Graph[a].append(b)
    Graph[b].append(a)

dist_T = [-1]*(N+1)  # uからの最短距離
dist_A = [-1]*(N+1)  # vからの最短距離
dist_T[u] = 0
dist_A[v] = 0

from collections import deque
q1 = deque([u])
q2 = deque([v])
while q1:
    n = q1.pop()
    for d in Graph[n]:
        if dist_T[d] == -1:
            dist_T[d] = dist_T[n] + 1
            q1.appendleft(d)
while q2:
    n = q2.pop()
    for d in Graph[n]:
        if dist_A[d] == -1:
            dist_A[d] = dist_A[n] + 1
            q2.appendleft(d)

ans = 0
for i in range(1,N+1):
    if dist_T[i] < dist_A[i]:
        ans = max(ans,dist_A[i]-1)

print(ans)
