N = input()

dp = [0, 1]
for n in N:
  n = int(n)
  dp[0], dp[1] = min(dp[0]+n, dp[1]+10-n), min(dp[0]+n+1, dp[1]+10-(n+1))

print(dp[0])