def cmb(n,r,mod):
  if r<0 or r>n:
    return 0
  r=min(r,n-r)
  return g1[n]*g2[r]*g2[n-r]%mod

k=int(input())
s=list(input())
n=len(s)
mod=10**9+7

g1=[1,1]
g2=[1,1]
inverse=[0,1]

for i in range(2,2*10**6+1):
  g1.append((g1[-1]*i)%mod)
  inverse.append((-inverse[mod%i]*(mod//i))%mod)
  g2.append((g2[-1]*inverse[-1])%mod)

pow25=[1]
for i in range(n+k+1):
  pow25.append((pow25[-1]*25)%mod)

pow26=[1]
for i in range(n+k+1):
  pow26.append((pow26[-1]*26)%mod)

ans=0
for i in range(n,n+k+1):
  ans+=cmb(i-1,n-1,mod)*pow25[i-n]*pow26[n+k-i]
  ans%=mod
print(ans)