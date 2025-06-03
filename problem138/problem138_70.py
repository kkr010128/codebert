MOD = 998244353

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0 for j in range(S + 1)] for i in range(N + 1)]
dp[0][0] = 1

p = [[0 for k in range(N + 1)] for j in range(S + 1)]
p[0][0] = 1

for i in range(N):
    for j in range(S + 1):
        dp[i + 1][j] += dp[i][j] * 2
        p[j]
        if j >= A[i]:
            dp[i + 1][j] += dp[i][j - A[i]]
        dp[i + 1][j] %= MOD

print(dp[N][S])