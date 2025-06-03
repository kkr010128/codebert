n = int(input())

mod = 10 ** 9 + 7
dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n)]
dp[0][0][0] = 8
dp[0][0][1] = 1
dp[0][1][0] = 1
dp[0][1][1] = 0

for i in range(n-1):
    for j in range(2):
        dp[i+1][0][0] = (dp[i][0][0] * 8) % mod
        dp[i+1][0][1] = (dp[i][0][0] + dp[i][0][1] * 9) % mod
        dp[i+1][1][0] = (dp[i][0][0] + dp[i][1][0] * 9) % mod
        dp[i+1][1][1] = (dp[i][0][1] + dp[i][1][0] + dp[i][1][1] * 10) % mod

print((dp[-1][-1][-1]) % mod)