#AC

from collections import deque

n=int(input())
G=[[]]
for i in range(n):
    G.append(list(map(int,input().split()))[2:])

#bfs(木でないかも)
L=[-1]*(n+1)
q=deque()

L[1]=0
q.append(1)
while q:
    now=q.popleft()
    L.append(now)
    for next in G[now]:
        #探索済み
        if L[next]>=0:
            continue
        #探索予定(なくて良い)
        #if next in q:
        #    continue
        q.append(next)
        L[next]=L[now]+1

for i in range(1,n+1):
    print(i,L[i])

