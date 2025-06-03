mod = 10**9 + 7
  
n = int(input())
dp = [0]*(n+1)
dp[0] = 1

if n >= 3:
  for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-3]

print(dp[n] % mod)