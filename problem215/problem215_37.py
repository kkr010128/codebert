n, k = map(int, input().split())
MOD = 1000000007


def combinations(n, r, MOD):
    if (r < 0) or (n < r):
        return 0

    r = min(r, n - r)
    return fact[n] * fact_inv[r] * fact_inv[n - r] % MOD


fact = [1, 1]
fact_inv = [1, 1]
inv = [0, 1]

for i in range(2, n + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    fact_inv.append((fact_inv[-1] * inv[-1]) % MOD)


s = 0
for num_zero in range(min(k + 1, n)):
    # nCz
    x = combinations(n, num_zero, MOD)

    # n-zCx
    y = combinations(n - 1, n - num_zero - 1, MOD)

    s += (x * y) % MOD


print(s % MOD)
