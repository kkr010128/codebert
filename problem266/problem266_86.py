N=int(input())
coins = [100,101,102,103,104,105]
dp = [int(i%coins[0]==0) for i in range(N+1)]
for coin in coins[1:]:
  for i in range(coin,N+1):
    dp[i] += dp[i - coin]
if dp[-1] != 0:
  print(1)
else:
  print(0)