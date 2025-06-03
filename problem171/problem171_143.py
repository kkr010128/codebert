n = int(input())
a_ = [int(i) for i in input().split()]
a = [[a_[i], i+1] for i in range(n)]
a.sort(reverse=True)

dp = [[0 for i in range(n+1)] for j in range(n+1)]
ans = 0
for x_plus_y in range(n):
    for x in range(x_plus_y + 1): #x：左に詰めた個数
        y = x_plus_y - x #y：# 右に詰めた個数
        dp[x][y+1] = max(dp[x][y+1], a[x_plus_y][0] * abs((n - y) - a[x_plus_y][1]) + dp[x][y]) #右
        dp[x+1][y] = max(dp[x+1][y], a[x_plus_y][0] * abs((a[x_plus_y][1] - (1+x))) + dp[x][y]) #左

        if x_plus_y == n-1:
            ans = max(ans, dp[x][y+1], dp[x+1][y])

print(ans)