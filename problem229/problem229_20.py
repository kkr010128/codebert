h, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

INF = 1 << 60

dp = [INF] * (h + 1)
dp[0] = 0

for i in range(0, h + 1):
    #　hを超えるために必要な最小コストは？
    for a, b in ab:
        if i + a <= h:
            dp[i + a] = min(dp[i] + b, dp[i + a])
        else:
            dp[h] = min(dp[i] + b, dp[h])

print(dp[h])