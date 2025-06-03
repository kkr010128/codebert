k = int(input())
s = input()

mod = 10**9+7

def fpow(x, y):
  res = 1
  while y>0:
    if y%2 == 1:
      res = (res%mod * x%mod)%mod
    x = (x%mod * x%mod)%mod
    y = y//2
  return res
MAXN = 2000005
fact = [0]*MAXN
fact[0] = 1
for i in range(1, MAXN):
  fact[i] = (i%mod * fact[i-1]%mod)%mod
  
def inv(a):
  return fpow(a, mod-2)
  
n = len(s)
ans = fpow(26, n+k)
for m in range(n):
    ncm = (fact[n+k]%mod * inv(fact[m])%mod)%mod
    ncm = (ncm%mod * inv(fact[n+k-m])%mod)%mod
    
    p = fpow(25, n+k-m)
    
    val = (ncm%mod * p%mod)%mod
    
    ans = (ans%mod - val%mod + mod)%mod
print(ans%mod)