K = int(input())
S = input()
n = len(S)
MOD = 10 ** 9 + 7
MAX = 2 * 10 ** 6 + 5

fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX
fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1
for i in range(2, MAX):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD

def nCk(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

A = 0
for i in range(K + 1):
    A1 = pow(26, K - i, MOD)
    A2 = (pow(25, i, MOD) * nCk(i + n - 1, n - 1)) % MOD
    A = (A + (A1 * A2) % MOD) % MOD

print(A % MOD)