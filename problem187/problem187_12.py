n,x,y=map(int,input().split())
l=[]
for i in range(n-1):
  for j in range(i+1,n):
    d1=j-i
    d2=abs((x-1)-i)+abs(j-(y-1))+1
    d=min(d1,d2)
    l.append(d)
import collections
c=collections.Counter(l)
for kk in range(1,n):
  print(c[kk])