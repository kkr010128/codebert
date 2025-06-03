def cmb(n, r, p):
  if (r < 0) or (n < r):
    return 0
  r = min(r, n - r)
  return fac[n]*finv[r]*finv[n-r]%p

N = pow(10,6)
MOD = pow(10,9)+7

fac = [-1]*(N+1); fac[0] = 1; fac[1] = 1 #階乗
finv = [-1]*(N+1); finv[0] = 1; finv[1] = 1 #階乗の逆元
inv = [-1]*(N+1); inv[0] = 0; inv[1] = 1 #逆元
for i in range(2,N+1):
  fac[i] = fac[i-1]*i%MOD
  inv[i] = MOD - inv[MOD%i]*(MOD//i)%MOD
  finv[i] = finv[i-1]*inv[i]%MOD


X,Y = map(int,input().split())
if (X+Y)%3 != 0:
  print(0)
  exit()
n = (X+Y)//3
if min(X,Y) < n:
  print(0)
  exit()

ans = cmb(n,min(X,Y)-n,MOD)
print(ans)