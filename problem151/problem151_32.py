# Problem E - Colorful Blocks

# input
N, M, K = map(int, input().split())

# initialization
MOD = 998244353
fact = [1, 1]
fact_inv = [1, 1]
inv = [0, 1]
pow_list = [1, M-1]
for i in range(2, N+1):
    fact.append((fact[-1] * i)%MOD)
    inv.append((-inv[MOD%i] * (MOD//i))%MOD)
    fact_inv.append((fact_inv[-1] * inv[-1])%MOD)
    pow_list.append(pow_list[i-1]*(M-1)%MOD)

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n-r)
    return fact[n] * fact_inv[r] * fact_inv[n-r] % p

ans = 0

# calc
for i in range(K+1):
    tmp = ((M * cmb(N-1, i, MOD))%MOD * pow_list[N-(i+1)])%MOD
    ans = (ans + tmp)%MOD

# output
print(ans)
