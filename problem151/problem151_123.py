N,M,K=list(map(int,input().split()))

MAXN = 2*(10**5)+10
p = 998244353
MOD = p
f = [1]
for i in range(MAXN):
    f.append(f[-1] * (i+1) % MOD)
def nCr(n, r, mod=MOD):
    return f[n] * pow(f[r], mod-2, mod) * pow(f[n-r], mod-2, mod) % mod

def power_func(a,n,p):
  bi=str(format(n,"b"))#2進表現に
  res=1
  for i in range(len(bi)):
    res=(res*res) %p
    if bi[i]=="1":
      res=(res*a) %p
  return res

out = 0
for i in range(K+1):
    out += M*nCr(N-1,i,p)*power_func(M-1,N-1-i,p)
    out = out % p
print(out)