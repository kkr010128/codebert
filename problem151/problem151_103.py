n, m, k = map(int, input().split())

mod = 998244353
fact = [1] * (n + 1)
ifact = [1] * (n + 1)

for i in range(n):
    fact[i + 1] = fact[i] * (i + 1) % mod
    ifact[i + 1] = pow(fact[i + 1], mod - 2, mod)


def comb(x, y):
    if y < 0 or y > x:
        return 0
    return (fact[x] * ifact[x - y] * ifact[y]) % mod


mm = [1]
for _ in range(n + 1):
    mm.append(mm[-1] * (m - 1) % mod)

ans = 0
for i in range(k + 1):
    ans += m * comb(n - 1, i) * mm[n - 1 - i]
    ans %= mod

print(ans)
