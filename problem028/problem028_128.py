n, m = map(int, raw_input().split())
c = map(int, raw_input().split())
dp = [n+1] * (n+1)
dp[n] = 0
for rest in xrange(n, 0, -1):
    for i in xrange(m):
        if c[i] <= rest:
            dp[rest - c[i]] = min(dp[rest - c[i]], 1 + dp[rest])
print dp[0]