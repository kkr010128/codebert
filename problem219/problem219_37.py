N = [int(c) for c in input()]
dp = 0,1
for n in N:
  a = min(dp[0]+n,dp[1]+10-n)
  b = min(dp[0]+n+1,dp[1]+10-(n+1))
  dp = a,b
print(dp[0])