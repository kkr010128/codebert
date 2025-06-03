# YouTube解説
MOD = 1000000007
n, k = [int(x) for x in input().split()]
d = [0] * (k + 1)

for i in range(1, k + 1):
    d[i] = pow(k // i, n, MOD)

for i in range(k, 0, -1):  # 大きいほうから
    for j in range(i * 2, k + 1, i):  # iの倍数
        # d[6] = d'[6] - d[12] - d[18] ...
        d[i] -= d[j]
        d[i] %= MOD
ans = 0
for i, item in enumerate(d):
    ans += i * item
    ans %= MOD
print(ans)
