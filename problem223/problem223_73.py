N,K=map(int,input().split())
P=list(map(int,input().split()))
from itertools import accumulate
acc=[0]
acc.extend(accumulate(P))
ans=0
for i in range(N-K+1):
  exp=(acc[K+i]-acc[i]+K)/2
  ans=max(exp,ans)
print(ans)