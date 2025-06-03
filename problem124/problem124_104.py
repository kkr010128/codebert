K = int(input())
s = len(input())

mod = 10 ** 9 + 7
N = 2 * 10**6
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
  fac.append( ( fac[-1] * i ) % mod )
  inv.append( mod - ( inv[mod % i] * (mod // i) % mod ) )
  finv.append( finv[-1] * inv[-1]  % mod )

def cmb(n, r):
  return fac[n] * ( finv[r] * finv[n-r] % mod ) % mod

p25 = [1]
p26 = [1]

for i in range(K):
  p25.append(p25[i]*25%mod)
  p26.append(p26[i]*26%mod)

ans = 0

for i in range(K+1):
  ans += ( cmb(s+K-i-1, s-1) * p25[K-i] % mod ) * p26[i] % mod
  ans %= mod

print(ans)