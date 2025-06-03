n = input()
l = list(map(int, str(n)))

dp = [[0] * 2 for _ in range(len(l)+1)]
dp[0][1] = 1

for i, v in enumerate(l):
    dp[i+1][0] = min(dp[i][0] + v, dp[i][1] + (10 - v))
    dp[i+1][1] = min(dp[i][0] + v + 1, dp[i][1] + (10 - v) - 1)

print(dp[-1][0])