mod = 998244353

n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(s + 1)] for _ in range(n + 1)]
dp[0][0] = 1
for i, num in enumerate(a, start = 1):
    for j in range(s + 1):
        dp[i][j] = (dp[i - 1][j] * 2) % mod
        if j - num >= 0:
            dp[i][j] += dp[i - 1][j - num]

print(dp[-1][-1] % mod)