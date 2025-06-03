N, T = map(int, input().split())
AB = sorted([list(map(int, input().split())) for _ in range(N)])

dp = [[0] * N for _ in range(T)]

for i in range(1, T):
    for j in range(N-1):
        if AB[j][0] <= i:
            dp[i][j] = max(dp[i][j-1], dp[i-AB[j][0]][j-1] + AB[j][1])
        else:
            dp[i][j] = dp[i][j-1]

ans = 0
for j in range(1, N):
    ans = max(ans, dp[-1][j-1] + AB[j][1])

print(ans)