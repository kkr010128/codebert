N,K=map(int,input().split())
ans=[0]*(K+1)
mod=10**9+7
for i in range(K,0,-1):
  ans[i]=pow((K//i),N,mod)
  ind=2
  while i*ind<=K:
    ans[i]-=ans[i*ind]
    ans[i]%=mod
    ind+=1
res=0
for i in range(1,K+1):
  res+=i*ans[i]
  res%=mod
print(res)