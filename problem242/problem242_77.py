MOD = 10 ** 9 + 7
fac = [1] * (10 ** 5 + 10)
for i in range(len(fac) - 1):
    fac[i + 1] = fac[i] * (i + 1) % MOD


def comb(n, k):
    return fac[n] * pow(fac[n - k], MOD - 2, MOD) * pow(fac[k], MOD - 2, MOD) % MOD


n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(k - 1, n):
    ans += comb(i, k - 1) * a[i]
for i in range(n - k + 1):
    ans -= comb(n - i - 1, k - 1) * a[i]
print(ans % MOD)
