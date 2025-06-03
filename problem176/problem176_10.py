n,k=map(int,input().split())
mod=10**9+7
ans=0
A=[0]*k
for i in range(k,0,-1):
  a=0
  A[i-1]=pow((k//i),n,mod)
  m=i*2
  while m<=k:
    A[i-1]=(A[i-1]-A[m-1])%mod
    m=m+i
  ans=(ans+i*A[i-1])%mod
print(ans%mod)