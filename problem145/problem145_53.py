from collections import deque

N,M =map(int,input().split())
graph=[[] for _ in range(N)]

for _ in range(M):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    graph[a].append(b)
    graph[b].append(a)

dist=[-1]*N
pre=[-1]*N
dist[0]=0

q=deque()
q.append(0)

while q:
    v=q.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        else:
            dist[i]=dist[v]+1
            pre[i]=v
            q.append(i)

print("Yes")
for i in range(1,N):
    print(pre[i]+1)