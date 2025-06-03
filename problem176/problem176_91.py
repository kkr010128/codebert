n, k = map(int, input().split())
MOD = 1000000007
ans = 0
c = {}
for i in range(k, 0, -1):
    t = pow(k // i, n, MOD)
    m = 2
    while i * m <= k:
        t -= c[i * m]
        m += 1
    c[i] = t % MOD
print(sum([k * v for k, v in c.items()]) % MOD)
