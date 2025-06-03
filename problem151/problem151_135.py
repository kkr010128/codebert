n,m,k=map(int,input().split())
mod=998244353
ans=m*pow(m-1,n-1,mod)
ans%=mod

if k==0:
  print(ans)
  exit()

lst=[1]+[1]
for i in range(2,n+10):
  lst.append((lst[-1]*i)%mod)

def combinations(n,r):
  xxx=lst[n]
  xxx*=pow(lst[n-r],mod-2,mod)
  xxx%=mod
  xxx*=pow(lst[r],mod-2,mod)
  xxx%=mod

  return xxx


for i in range(1,k+1):
    ans+=(m*pow(m-1,n-1-i,mod)*combinations(n-1,i))%mod
    ans%=mod


print(ans)
