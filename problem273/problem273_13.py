n,k=map(int,input().split())
a=[0]+list(map(int,input().split()))
for i in range(n):a[i+1]=(a[i+1]+a[i]-1)%k
from collections import defaultdict
d=defaultdict(int)
x=0
d[0]=1
for i in range(1,n+1):
  if i-k>=0:d[a[i-k]]-=1
  x+=d[a[i]]
  d[a[i]]+=1
print(x)