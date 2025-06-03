from collections import defaultdict
d=defaultdict(int)
n=int(input())
a=list(map(int,input().split()))
ans=1
mod=10**9+7
d[-1]=3
for i in a:
  ans*=d[i-1]
  ans%=mod
  d[i-1]-=1
  d[i]+=1
print(ans)