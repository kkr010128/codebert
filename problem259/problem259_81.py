import sys
input = sys.stdin.readline
n,u,v=map(int, input().split())
u-=1
v-=1
es=[[] for i in range(n)]
for i in range(n-1):
    a0,b0=map(int, input().split())
    es[a0-1].append(b0-1)
    es[b0-1].append(a0-1)
aoki=[-1]*n
aoki[v]=0
choku=[-1]*n
choku[u]=0
from collections import deque
que=deque([])
que.append(u)
while que:
    now=que.popleft()
    step=choku[now]
    for e in es[now]:
        if choku[e]==-1:
            choku[e]=step+1
            que.append(e)

que=deque([])
que.append(v)
while que:
    now=que.popleft()
    step=aoki[now]
    for e in es[now]:
        if aoki[e]==-1:
            aoki[e]=step+1
            que.append(e)

end=None
for i in range(n):
    if len(es[i])==1: 
        if choku[i]==0 and aoki[i]==1:
            print(0)
            exit()
        elif end==None and aoki[i]>choku[i]:
            end=(i, aoki[i])
        elif aoki[i]>choku[i] and end[1]<aoki[i]:
            end=(i, aoki[i])
print(end[1]-1)