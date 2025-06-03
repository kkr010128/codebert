n, m = map(int, input().split())
D = list(map(int, input().split()))

INF = int(1e18)

# dp[i]: i円をDで支払うときの最小枚数
dp = [INF] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for d in D:
        if i - d >= 0:
            dp[i] = min(dp[i], dp[i - d] + 1)
        else:
            dp[i] = dp[i]

print(dp[n])
