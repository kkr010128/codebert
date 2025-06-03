max_n=10**5
mod=10**9+7

frac=[1]
for i in range(1,max_n+1):
  frac.append((frac[-1]*i)%mod)

inv=[1,1]
inv_frac=[1,1]
for i in range(2,max_n):
  inv.append((mod-inv[mod%i]*(mod//i))%mod)
  inv_frac.append((inv_frac[-1]*inv[-1])%mod)
  
def perm(m,n):
  if m<n:
    return 0
  if m==1:
    return 1
  return (frac[m]*inv_frac[m-n])%mod

def comb(m,n):
  if m<n:
    return 0
  if m==1:
    return 1
  return (frac[m]*inv_frac[n]*inv_frac[m-n])%mod

s=int(input())
c=0
for i in range(1,s//3+1):
  ss=s-i*3
  c=(c+comb(ss+i-1,i-1))%mod
print(c)