from collections import deque
n,m=map(int,input().split())
e=[[] for _ in range(n+1)]
lndmrk=[-1]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    e[a].append(b)
    e[b].append(a)
q=deque()
lndmrk[1]=0
q.append(1)
while(len(q) !=0):
    v=q.popleft()
    for i in e[v]:
        if lndmrk[i]==-1:
            lndmrk[i]=v
            q.append(i)
f=True
for i in range(2,n+1):
    if lndmrk[i]==-1:
        f=False
        break
if f:
    print('Yes')
    for i in range(2,n+1):
        print(lndmrk[i])
else:
    print('No')
