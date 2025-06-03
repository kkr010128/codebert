MOD = 998244353
N, K = map(int, input().split())
rl = [list(map(int, input().split())) for _ in range(K)]
dp = [0] * (N + 1)
dp[1] = 1
dp[2] = -1

for i in range(1, N + 1):
    dp[i] += dp[i - 1]
    for j in range(K):
        l, r = rl[j][0], rl[j][1]
        if i + l <= N:
            dp[i + l] += dp[i]
            dp[i + l] %= MOD
        if i + r + 1 <= N:
            dp[i + r + 1] -= dp[i]
            dp[i + r + 1] %= MOD
print(dp[N] % MOD)