from collections import deque
INFTY = 10**6
N,u,v = map(int,input().split())
G = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
du = [INFTY for _ in range(N+1)]
du[u] = 0
que = deque([(0,u)])
hist = [0 for _ in range(N+1)]
hist[u] = 1
while que:
    c,i = que.popleft()
    for j in G[i]:
        if hist[j]==0:
            que.append((c+1,j))
            du[j] = c+1
            hist[j] = 1
dv = [INFTY for _ in range(N+1)]
dv[v] = 0
que = deque([(0,v)])
hist = [0 for _ in range(N+1)]
hist[v] = 1
while que:
    c,i = que.popleft()
    for j in G[i]:
        if hist[j]==0:
            que.append((c+1,j))
            dv[j] = c+1
            hist[j] = 1
cmax = 0
for i in range(1,N+1):
    if du[i]<dv[i]:
        cmax = max(cmax,dv[i])
print(cmax-1)