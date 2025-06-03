x,y,a,b,c=map(int, input().split())
*p,=map(int, input().split())
*q,=map(int, input().split())
*r,=map(int, input().split())
from heapq import *
p=[-i for i in p]
q=[-i for i in q]
r=[-i for i in r]
heapify(p)
heapify(q)
heapify(r)
ans=0
cnt=0
pt=heappop(p)
qt=heappop(q)
rt=heappop(r)
n=x+y
while (x>=0 or y>=0) and cnt<n:
  if rt==0:
    if pt<=qt:
      ans-=pt
      x-=1
      cnt+=1
      if p and x>0: pt=heappop(p)
      else: pt=0
    else:
      ans-=qt
      y-=1
      cnt+=1
      if q and y>0: qt=heappop(q)
      else: qt=0
  elif pt<=rt:
    ans-=pt
    x-=1
    cnt+=1
    if p and x>0: pt=heappop(p)
    else: pt=0
  elif qt<=rt:
    ans-=qt
    y-=1
    cnt+=1
    if q and y>0: qt=heappop(q)
    else: qt=0
  else:
    ans-=rt
    cnt+=1
    if r: rt=heappop(r)
    else: rt=0
print(ans)
