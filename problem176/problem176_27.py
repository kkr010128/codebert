n, k = map(int, input().split())
MOD = 10 ** 9 + 7

cnt = [0] * (k + 1)
for num in range(1, k + 1):
    cnt[num] = pow((k // num), n, MOD)

for num in range(1, k + 1)[::-1]:
    for i in range(2, k // num + 1):
        cnt[num] -= cnt[num * i]
        cnt[num] % MOD

ans = 0
for num in range(1, k + 1):
    ans += cnt[num] * num
    ans %= MOD
print(ans)
