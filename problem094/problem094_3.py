R, C, K = map(int, input().split())
items = [[0]*C for _ in range(R)]

for i in range(K):
  r, c, v = map(int, input().split())
  items[r-1][c-1] = v

dp = [[0]*4 for _ in range(C)]

for x in range(1, 4):
  dp[0][x] = items[0][0]
  for j in range(1, C):
    dp[j][x] = max(dp[j-1][x-1] + items[0][j], dp[j-1][x])

#print(items)
#print(dp)

for i in range(1, R):
  for j in range(C):
    for x in range(4):
      dp[j][x] = dp[j][3]
  for x in range(1, 4):
    dp[0][x] += items[i][0]
    for j in range(1, C):
      dp[j][x] = max(dp[j-1][x-1] + items[i][j], dp[j-1][x], dp[j][3] + items[i][j])
  #print(dp)

print(dp[-1][-1])