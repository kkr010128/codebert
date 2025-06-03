from collections import deque
n,m=map(int,input().split())
node=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    node[b-1].append(a-1)
    node[a-1].append(b-1)
distance=[-1]*n
distance[0]=0

d=deque()
d.append(0)
while d:
    v=d.popleft()
    for i in node[v]:
        if distance[i]!=-1:
            continue
        distance[i]=v+1
        d.append(i)
print('Yes')
for i in range(1,n):
    print(distance[i])