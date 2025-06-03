X = int(input())

dp = [0] * 110000
dp[100] = 1
dp[101] = 1
dp[102] = 1
dp[103] = 1
dp[104] = 1
dp[105] = 1

for i in range(X + 1):
    dp[i + 100] = max(dp[i], dp[i + 100])
    dp[i + 101] = max(dp[i], dp[i + 101])
    dp[i + 102] = max(dp[i], dp[i + 102])
    dp[i + 103] = max(dp[i], dp[i + 103])
    dp[i + 104] = max(dp[i], dp[i + 104])
    dp[i + 105] = max(dp[i], dp[i + 105])

print(dp[X])