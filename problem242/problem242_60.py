n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
mod=10**9+7
f=[1]
for i in range(n):f+=[f[-1]*(i+1)%mod]
def comb(a,b):return f[a]*pow(f[b],mod-2,mod)*pow(f[a-b],mod-2,mod)%mod
ans=0
for i in range(n-k+1):
  t=a[-1-i]
  ans=(ans+t*comb(n-i-1,k-1))
  ans%=mod
a=a[::-1]
for i in range(n-k+1):
  t=a[-1-i]
  ans=(ans-t*comb(n-i-1,k-1))
  ans%=mod
print(ans)