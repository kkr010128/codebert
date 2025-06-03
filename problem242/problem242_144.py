N, K = map(int, input().split())
A = list(map(int, input().split()))


mod = 10 ** 9 + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]


def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)


A.sort()
ans = 0
for i, (n, x) in enumerate(zip(A, A[::-1])):
    if i < K-1:
        continue
    ans += n * cmb(i, K - 1)
    ans %= mod
    ans -= x * cmb(i, K - 1)
    ans %= mod
print(ans)
