MAX = 1000000
MOD = 1000000007

fac = [None] * MAX
finv = [None] * MAX
inv = [None] * MAX

def comb_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

def comb(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

comb_init()
X, Y = map(int, input().split())

n = (2 * Y - X) // 3
m = (2 * X - Y) // 3

if (X + Y) % 3 != 0 or n < 0 or m < 0:
    print(0)
    exit()

print(comb(n + m, n))
