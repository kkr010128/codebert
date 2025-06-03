n = input()
n = n[::-1]
n += '0'
cnt = 0
dp = [[float('inf')] * 2 for _ in range(len(n) + 1)]
dp[0][0] = 0
dp[0][1] = 1
for i in range(len(n)):
    a = int(n[i])
    dp[i + 1][0] = min(dp[i][0] + a, dp[i][1] + a + 1)
    dp[i + 1][1] = min(dp[i][0] + 10 - a, dp[i][1] + 10 - (a + 1))
print(min(dp[len(n)][0], dp[len(n)][1]))