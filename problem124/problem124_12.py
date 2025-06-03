MAX = 2*10**6
MOD = 10**9+7

fac = [0] * (MAX)
finv = [0] * (MAX)
inv = [0] * (MAX)

def comb_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD

def comb(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD


if __name__ == '__main__':
    k = int(input())
    s = input()
    n = len(s)
    comb_init()
    ans = 0
    for i in range(k+1):
        val = comb(i+n-1, n-1)
        val *= pow(25, i, MOD)
        val %= MOD
        val *= pow(26, k-i, MOD)
        val %= MOD
        ans += val
        ans %= MOD
    print(ans)
