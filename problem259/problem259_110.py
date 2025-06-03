from collections import deque
infinity=10**6

import sys
input = sys.stdin.readline
N,u,v = map(int,input().split())
u -= 1
v -= 1

G=[[] for i in range(N)]
for i in range(N-1):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

ends = []
for i in range(N):
    if len(G[i]) == 1:
        ends.append(i)

#幅優先探索
def BFS (s):
    queue = deque()
    d = [infinity]*N
    
    queue.append(s)
    d[s]= 0
    
    while len(queue)!=0:
      u = queue.popleft()
      for v in G[u]:
      	if d[v] == infinity:
        	d[v] = d[u]+1
        	queue.append(v) 	  


  
    return d

d_nigeru = BFS(u)
d_oni = BFS(v)

ans=0
for u in ends:
    if d_nigeru[u] < d_oni[u]:
        ans = max(ans,d_oni[u]-1)

print(ans)