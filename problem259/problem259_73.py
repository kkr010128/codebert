import sys
input=sys.stdin.readline
n,u,v = map(int, input().split())
link = [[] for _ in range(n)]
for i in range(n-1):
    tmp = list(map(int,input().split()))
    link[tmp[0]-1].append(tmp[1]-1)
    link[tmp[1]-1].append(tmp[0]-1)

from collections import deque
Q = deque()
Q.append([v-1,0])
visited=[-1]*n
visited[v-1]=0
while Q:
    now,cnt = Q.popleft()
    for nxt in link[now]:
        if visited[nxt]!=-1:
            continue
        visited[nxt]=cnt+1
        Q.append([nxt,cnt+1])
Q = deque()
Q.append([u-1,0])
v_taka=[-1]*n
v_taka[u-1]=0
while Q:
    now,cnt = Q.popleft()
    for nxt in link[now]:
        if v_taka[nxt]!=-1:
            continue
        if visited[nxt] <= cnt+1:
            continue
        v_taka[nxt]=cnt+1
        Q.append([nxt,cnt+1])
ans=-1
for i in range(n):
    if v_taka[i] == -1:
        continue
    if ans < visited[i]:
        ans=visited[i]
print(ans-1)