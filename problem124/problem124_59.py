MOD = 10**9+7

k = int(input())
s = input()
MAX = k + len(s)

factorial = [0] * (MAX + 1)
factorial[0] = 1
for i in range(1, MAX + 1):
    factorial[i] = factorial[i-1] * i % MOD


ifactorial = [0] * (MAX + 1)
ifactorial[MAX] = pow(factorial[MAX], MOD - 2, MOD)
for i in range(MAX, 0, -1):
    ifactorial[i - 1] = ifactorial[i] * i % MOD

pow25 = [1] * (k + 1)
pow26 = [1] * (k + 1)
for i in range(k):
    pow25[i + 1] = pow25[i] * 25
    pow25[i + 1] %= MOD
    pow26[i + 1] = pow26[i] * 26
    pow26[i + 1] %= MOD


def combination(n, k):
    ret = factorial[n] * ifactorial[k] * ifactorial[n - k]
    return ret % MOD


ans = 0
for i in range(k + 1):
    tmp = combination(i + len(s) - 1, len(s) - 1)
    tmp *= pow25[i]
    tmp %= MOD
    # tmp *= pow(25, i, MOD)
    tmp *= pow26[k - i]
    # tmp *= pow(26, k - i, MOD)
    tmp %= MOD
    ans += tmp
    ans %= MOD
print(ans)
