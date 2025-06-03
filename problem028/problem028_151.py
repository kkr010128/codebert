def solver(n ,m, coins):
  dp = [[100000] * (n + 1) for i in range(m + 1)]
  for i in range(m + 1): dp[i][0] = 0
  for r in range(1, m + 1):
    for c in range(1, n + 1):
      if 0 > c - coins[r - 1]:
        dp[r][c] = dp[r - 1][c]
      else:
        dp[r][c] = min(dp[r - 1][c], dp[r][c - coins[r - 1]] + 1)
  print(dp[m][n])


n, m = map(int, input().split())
coins = sorted(list(map(int, input().split())))
solver(n, m, coins)
