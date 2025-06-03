N, S = map(int, input().split())
A = list(map(int, input().split()))

MOD = 998244353

dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    ai = A[i]
    for j in range(S + 1):
        here = dp[i][j]
        # aiがTに含まれない
        dp[i + 1][j] += here
        # aiがTに含まれるが, Uに含まれない
        dp[i + 1][j] += here

        dp[i + 1][j] %= MOD

        # aiがUに含まれる
        if j + ai <= S:
            dp[i + 1][j + ai] += dp[i][j]
            dp[i + 1][j + ai] %= MOD

print(dp[N][S])
