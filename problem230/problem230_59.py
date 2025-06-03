n,d,a=[int(j) for j in input().split()]
xh=[[int(j) for j in input().split()] for i in range(n)]
xh.sort()
from collections import deque
q=deque()
ans=0
dmg=0
for x,h in xh:
    while q and q[0][0]<x:
        i,j=q.popleft()
        dmg-=j
    r=h-dmg
    if r<=0:
        continue
    p=-(-r//a)
    dmg+=p*a
    ans+=p
    q.append((x+2*d,p*a))
print(ans)




