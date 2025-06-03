from collections import deque

N,M=map(int,input().split())
G=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

group=[]
seen=[0]*N
ans=0
for i in range(N):
    if seen[i]: continue
    que=deque()
    seen[i]=1
    cnt=0
    que.append(i)
    while que:
        cnt+=1
        v=que.popleft()
        for nv in G[v]:
            if seen[nv]: continue
            seen[nv]=1
            que.append(nv)
    ans=max(ans,cnt)

print(ans)
