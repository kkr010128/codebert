n, t = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(n)]

ab = sorted(ab, key=lambda x:(x[0]))

t -= 1
dp = [[0]*(t+1) for i in range(n+1)]
for i in range(1, n+1):
    ca, cb = ab[i-1][0], ab[i-1][1]
    for j in range(1, t+1):
        if j - ca >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-ca] + cb)
        else:
            dp[i][j] = dp[i-1][j]

b_max = [0]
tmp = 0
for i in range(n-1, -1, -1):
    tmp = max(tmp, ab[i][1])
    b_max = [tmp] + b_max

ans = 0
for i in range(n+1):
    ans = max(ans, dp[i][t] + b_max[i])
    # print(dp[i][t] + b_max[i])

print(ans)