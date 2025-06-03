N, S = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353

dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i, a in enumerate(A):
    for j in range(S + 1):
        dp[i + 1][j] += 2 * dp[i][j]
        dp[i + 1][j] %= MOD
        if j + a <= S:
            dp[i + 1][j + a] += dp[i][j]
            dp[i + 1][j + a] %= MOD

print(dp[-1][-1] % MOD)
