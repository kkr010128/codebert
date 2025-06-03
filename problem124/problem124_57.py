MOD = 10**9 + 7
N = 2 * 10**6 + 10  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod MOD)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod MOD)
inv = [0, 1]  

def nCr(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

k = int(input())
s = len(input())

ans = 0
for i in range(k+1):
    ansp =  pow(26,i,MOD) * pow(25,k-i,MOD) * nCr(s+k-1-i,s-1,MOD) % MOD 
    ans = (ans + ansp) % MOD
print(ans)
