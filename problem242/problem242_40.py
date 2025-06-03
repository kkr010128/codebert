n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7
a.sort()

fac = [1] * (n + 1)
inv = [1] * (n + 1)
def COMinit():
    for j in range(1, n + 1):
        fac[j] = fac[j - 1] * j % mod

    inv[n] = pow(fac[n], mod - 2, mod)
    for j in range(n - 1, -1, -1):
        inv[j] = inv[j + 1] * (j + 1) % mod

def comb2(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return fac[n] * inv[n - r] * inv[r] % mod

COMinit()
ans = 0
for i in range(n):
    x = comb2(n-1-i, k-1)
    ans = (ans - a[i]*x % mod) % mod
    ans = (ans + a[-1-i]*x % mod) % mod
print(ans%mod)

