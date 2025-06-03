n, k = map(int, input().split())
k = min(n - 1, k)

mod = 10 ** 9 + 7
fact = [1] * (n + 1)
ifact = [1] * (n + 1)

for i in range(n):
    fact[i + 1] = fact[i] * (i + 1) % mod
    ifact[i + 1] = pow(fact[i + 1], mod - 2, mod)


def comb(x, y):
    if y < 0 or y > x:
        return 0
    return (fact[x] * ifact[x - y] * ifact[y]) % mod


ans = 0
for i in range(k + 1):
    ans += comb(n, i) * comb(n - 1, n - i - 1) % mod
    ans %= mod
print(ans)
