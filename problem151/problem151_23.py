# -*- coding: utf-8 -*-
#https://mathtrain.jp/tyohukuc

n, m, k = map(int,input().split())

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 998244353
N = n+1 # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans = 0
beki = [1,m-1]
for i in range(2,N+1):
    beki.append(((beki[-1]*(m-1)) % p))

for x in range(k+1):
    ans += m * beki[n-x-1] %p * cmb(n-1,x,p) %p
    ans = ans % p
print(ans)
