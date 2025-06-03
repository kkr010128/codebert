a,b=map(int,input().split())
l=list(map(int,input().split()))
import itertools
b=min(b,50)
def ku(l):
    y=[0]*a
    for j,x in enumerate(l):
      y[max(0,j-x)]+=1
      r=min(j+x,a-1)
      if r<a-1:
        y[r+1]-=1
    return itertools.accumulate(y)

  
for _ in range(b):
  l=ku(l)
print(*l)