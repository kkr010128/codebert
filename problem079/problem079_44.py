S = int(input())
dp = (S+1)*[0]

for n in range(S+1):
  if 0<=n<=2:
    dp[n] = 0
  elif 3<=n<=5:
    dp[n] = 1
  else:
    dp[n] = (dp[n-3]+dp[n-1])%(10**9+7)

print(dp[S])