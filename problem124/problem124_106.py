MOD = 10 ** 9 + 7
M = 2 * 10 ** 6
fac = [1] * (M + 1)
for i in range(len(fac) - 1):
    fac[i + 1] = fac[i] * (i + 1) % MOD


def comb(n, k):
    return fac[n] * pow(fac[n - k], MOD - 2, MOD) * pow(fac[k], MOD - 2, MOD) % MOD


k = int(input())
s = input()
n = len(s)
ans = 0
for i in range(n, n + k + 1):
    ans += pow(25, n + k - i, MOD) * comb(n + k, i)
print(ans % MOD)
