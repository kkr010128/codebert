k = int(input())
s = input()
n = len(s)
MOD = 10**9+7
ans = 0

def comb(n, r, MOD):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % MOD

N = 2 * (10 ** 6) + 100
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

for i in range(k+1):
    b = pow(26, k-i, MOD)
    b *= pow(25, i, MOD)
    b *= comb(i+n-1, n-1, MOD)
    ans += (b % MOD)
    
print(ans%MOD)