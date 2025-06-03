x = int(input())
dp = [0] * 100200
dp[100] = 1
dp[101] = 1
dp[102] = 1
dp[103] = 1
dp[104] = 1
dp[105] = 1

for i in range(100, x+1):
    for p in [100, 101, 102, 103, 104, 105]:
        dp[i+p] = max(dp[i], dp[i+p])

print(dp[x])
