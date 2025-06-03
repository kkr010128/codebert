n, t = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort(key=lambda x: x[0])

dp = [[0] * (n+1) for i in range(t)]
ans = 0
for time in range(1, t):
    for i in range(n):
        if ab[i][0] <= time:
            if dp[time][i] < (ab[i][1] + dp[time - ab[i][0]][i]):
                dp[time][i+1] = (ab[i][1] + dp[ time - ab[i][0] ][i])
            else:
                dp[time][i+1] = dp[time][i]
        else:
            dp[time][i+1] = dp[time][i]
        if i < n-1:
            ans = max(ans, dp[time][i+1] + ab[i+1][1])

print(ans)
