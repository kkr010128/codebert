n,p=map(int,input().split())
s=list(map(int,list(input()[::-1])))
if p in [2,5]:
  ans=0
  for i in range(n):
    if s[-i-1]%p==0:ans+=i+1
  print(ans)
  exit()
from collections import defaultdict
d=defaultdict(int)
t=0
d[t]+=1
m=1
for i in range(n):
  t+=m*s[i]
  t%=p
  d[t]+=1
  m*=10
  m%=p
print(sum(d[i]*(d[i]-1)//2 for i in range(p)))