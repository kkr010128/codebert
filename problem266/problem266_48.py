X = int(input())

dp = [False]*(X+1)
dp[0] = True

for i in range(100, X+1):
  if i < 106:
    dp[i] = True
    continue
  if dp[i-100] or dp[i-101] or dp[i-102] or dp[i-103] or dp[i-104] or dp[i-105]:
    dp[i] = True

print(1) if dp[len(dp)-1] else print(0)