k = int(input())
s = input()
n = len(s)

N = n + k - 1

mod = 1000000007
fact = [1] * (N + 1)
ifact = [1] * (N + 1)

for i in range(N):
    fact[i + 1] = fact[i] * (i + 1) % mod
    ifact[i + 1] = pow(fact[i + 1], mod - 2, mod)


def comb(x, y):
    if y < 0 or y > x:
        return 0
    return (fact[x] * ifact[x - y] * ifact[y]) % mod


m25 = [1]
for i in range(k):
    m25.append(m25[i] * 25 % mod)
m26 = [1]
for i in range(k):
    m26.append(m26[i] * 26 % mod)

ans = 0
for i in range(k + 1):
    p = m25[k - i] * m26[i] % mod
    p *= comb(n + k - i - 1, n - 1)
    p %= mod
    ans += p
    ans %= mod
print(ans)
