from collections import deque

n,d,a = map(int, input().split())
ls = [list(map(int, input().split())) for i in range(n)]
ls.sort(key=lambda x:x[0])

q=deque()
ans=0
tot=0
for i in range(n):
    x=ls[i][0]
    h=ls[i][1]
    while q and q[0][0]<x:
        tot-=q[0][1]
        q.popleft()
    h-=tot
    if h>0:
        num = (h+a-1)//a
        ans+=num
        tot+=num*a
        q.append([x+2*d,num*a])

print(ans)