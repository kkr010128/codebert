n,k=map(int,input().split())
l=[i for i in range(1,k+1)][::-1]
mod=10**9+7
m=[0]*(k+1)
for i in l:
  a=k//i
  m[i]=pow(a,n,mod)
  for j in range(i*2,k+1,i):
    m[i]-=m[j]
ans=0
for i in range(k+1):
  ans+=m[i]*i
  ans%=mod
print(ans%mod)