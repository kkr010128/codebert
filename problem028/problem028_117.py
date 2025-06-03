INF = 10 ** 20

n, m = map(int, input().split())
c_lst = list(map(int, input().split()))

dp = [INF for _ in range(n + 1)]
dp[0] = 0
for coin in c_lst:
  for price in range(coin, n + 1):
    dp[price] = min(dp[price], dp[price - coin] + 1)

print(dp[n])
