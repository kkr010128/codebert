from collections import deque
N,M = map(int,input().split())
G = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
col = [-1 for _ in range(N+1)]
cnt = 0
for i in range(1,N+1):
    if col[i]<0:
        col[i]=cnt
        que = deque([i])
        while que:
            x = que.popleft()
            for y in G[x]:
                if col[y]<0:
                    col[y] = cnt
                    que.append(y)
        cnt += 1
C = {}
for i in range(1,N+1):
    a = col[i]
    if a not in C:
        C[a] = 0
    C[a] += 1
cmax = 0
for a in C:
    cmax = max(cmax,C[a])
print(cmax)