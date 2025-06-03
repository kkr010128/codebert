n, k = map(int, input().split())
MOD = 10 ** 9 + 7
cnt = [0] * (k + 1)

for gcd in range(1, k + 1):
    cnt[gcd] = pow(k // gcd, n, MOD)

for gcd in range(k, 0, -1):
    for i in range(2, k // gcd + 1):
        cnt[gcd] -= cnt[gcd * i]

ans = sum([num * c for num, c in enumerate(cnt)]) % MOD
print(ans)