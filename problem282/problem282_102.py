n, t = map(int, input().split())
dish = [list(map(int, input().split())) for _ in range(n)]
dish.sort(key=lambda x: x[0])
dp = [[0 for _ in range(3005)] for _ in range(3005)]

ans = 0
for i in range(n):
    for j in range(t):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        nj = j + dish[i][0]
        if nj < t:
            dp[i + 1][nj] = max(dp[i + 1][nj], dp[i][j] + dish[i][1])
    now = dp[i][t- 1] + dish[i][1]
    ans = max(ans, now)

print(ans)