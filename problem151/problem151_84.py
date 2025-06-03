n, m, k = map(int, input().split())

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n-r)
    return fact[n] *factinv[r]* factinv[n-r] %p

p = 998244353
N = 2 * 10**5 + 2

fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

y = [0,m]
for i in range(n):
    y.append((y[-1]*(m-1))%p)
r = 0
for i in range(k+1):
    r = (r + y[n-i]*cmb(n-1, i, p))%p
print(r)