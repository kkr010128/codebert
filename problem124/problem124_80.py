class Cmb:
  g1=[1,1]
  g2=[1,1]
  inv=[0,1]
  def __init__(self,mod,upper_limit):
    self.mod=mod
    for i in range(2,upper_limit+1):
      Cmb.g1.append(Cmb.g1[-1]*i%mod)
      Cmb.inv.append(-Cmb.inv[mod%i]*(mod//i)%mod)
      Cmb.g2.append(Cmb.g2[-1]*Cmb.inv[-1]%mod)
  def cmb(self,n,r):
    if r<0 or n<r:
      return 0
    r=min(r,n-r)
    return Cmb.g1[n]*Cmb.g2[r]*Cmb.g2[n-r]%self.mod

k=int(input())
s=len(input())
mod=10**9+7
Cmb=Cmb(mod,k+s)
ans=1
for i in range(1,k+1):
  ans=(ans*26+Cmb.cmb(i+s-1,s-1)*pow(25,i,mod))%mod
print(ans)