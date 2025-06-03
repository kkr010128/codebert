n = int(input())
a_ = [int(i) for i in input().split()]
a = [[a_[i], i+1] for i in range(n)]
a.sort(reverse=True)

dp = [[0 for i in range(n+1)] for j in range(n+1)]
x_plus_y = 0
ans = 0

for i in range(n):
    if x_plus_y == 0:
        dp[0][1] = a[i][0] * abs((n - a[i][1]))
        dp[1][0] = a[i][0] * abs((a[i][1] - 1))

    else:
        for x in range(x_plus_y + 1):
            y = x_plus_y - x
            dp[x][y+1] = max(dp[x][y+1], a[i][0] * abs((n - y) - a[i][1]) + dp[x][y])
            dp[x+1][y] = max(dp[x+1][y] , a[i][0] * abs((a[i][1] - (1+x))) + dp[x][y])

            if x_plus_y == n-1:
                ans = max(ans, dp[x][y+1], dp[x+1][y])

    x_plus_y += 1

print(ans)
