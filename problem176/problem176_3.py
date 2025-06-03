N,K=map(int,input().split())
ans=0
mod=10**9+7
A=[0 for i in range(K)]
for i in range(K,0,-1):
  l=pow(K//i,N,mod)
  a=2
  while a*i<=K:
    l-=A[a*i-1]
    a+=1
  ans+=l*i%mod
  ans%=mod
  A[i-1]=l
print(ans)