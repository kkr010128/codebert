MOD = 10**9 + 7
N, K = map(int, input().split())

dp = [0 for _ in range(K + 1)]
res = 0

for i in range(1, K + 1)[::-1]:
    dp[i] += pow(K // i, N, MOD)
    for j in range(1, K // i):
        dp[i] -= dp[i * (j + 1)]
    res += i * dp[i]
    res %= MOD

print(res)