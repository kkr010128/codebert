K = int(input())
S = input()
s = len(S)
L = []

mod = 10 ** 9 + 7
N = 2 * 10**6
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]

def cmb(n, r):
  return fac[n] * ( finv[r] * finv[n-r] % mod ) % mod
 
for i in range(2, N + 1):
  fac.append( ( fac[-1] * i ) % mod )
  inv.append( mod - ( inv[mod % i] * (mod // i) % mod ) )
  finv.append( finv[-1] * inv[-1]  % mod )

for i in range(K+1):
  L.append( cmb(i+s-1, s-1) * pow(25, i, mod) % mod )

ans = []

for i, x in enumerate(L):
  if i == 0:
    ans.append(x)
  else:
    ans.append( ( ans[i-1]*26%mod + x ) % mod )

print(ans[K])