n, m = [int(x) for x in raw_input().split()]
c = [int(x) for x in raw_input().split()]

INF = float("inf")
dp = [INF for i in xrange(n + 1)]
dp[0] = 0
for i in xrange(1, n + 1):
    for j in xrange(m):
        if c[j] <= i:
            dp[i] = min(dp[i], dp[i - c[j]] + 1)

print dp[n]