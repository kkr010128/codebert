s = int(input())
dp = [0]*(2001)
dp[3] = 1
mod = 10**9+7
for i in range(4,s+1):
    dp[i] = (dp[i-1] + dp[i-3]) % mod
print(dp[s])