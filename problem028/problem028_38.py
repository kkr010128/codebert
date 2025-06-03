n, m = map(int, raw_input().split())
l = map(int, raw_input().split())
INF = 1<<31
dp = [INF]*(n+1)
dp[0] = 0
for c in l:
    for i in range(n-c+1):
        if dp[i] != INF:
            dp[i + c] = min(dp[i] + 1, dp[i + c])
print dp[n]