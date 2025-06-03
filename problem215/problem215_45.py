n,k=map(int,input().split())
k=min(k,n-1)
mod=10000*100000+7
def mpow(a,b,m=100000*10000+7):#returns a**b%m
  ret=1
  while b>0:
    if b&1:
      ret=(ret*a)%m
    a=(a*a)%m
    b>>=1
  return ret
fact=[1]*(n+1)
ifact=[1]*(n+1)
for i in range(2,n+1):
  fact[i]=(fact[i-1] *i)%mod
ifact[n]=mpow(fact[n],mod-2)
for i in range(n-1,1,-1):
  ifact[i]=((i+1)*ifact[i+1])%mod
def nCr(n,r):
  if r==0 or r==n:
    return 1
  val=(fact[n]*ifact[r])%mod
  return (val*ifact[n-r])%mod
ans=0
for h in range(k+1):
  ans=(ans+(nCr(n,h)*nCr(n-1,n-h-1))%mod)%mod
print(ans)
