N,K=map(int,input().split())
mod=10**9+7

def cmb(n,r):
  global mod
  if r<0 or r>n:
    return 0
  return (g1[n]*g2[r]*g2[n-r])%mod

g1=[1,1]
g2=[1,1]
inv=[0,1]
for i in range(2,1000003):
  g1.append((g1[-1]*i)%mod)
  inv.append((-inv[mod%i]*(mod//i))%mod)
  g2.append((g2[-1]*inv[-1])%mod)
P=0
for i in range(min(N,K+1)):
  P=(P+cmb(N,i)*cmb(N-1,i))%mod
print(P)