n, t = map(int, input().split())
l = [[0, 0] for _ in range(n)]
 
for i in range(n):
  a, b = map(int, input().split())
  l[i][0] = a
  l[i][1] = b

l.sort()
#print(l)

ans = 0
dp = [[0]*(t+1) for _ in range(n+1)]
for i in range(n):
  for j in range(t):
    dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    nj = j+l[i][0]
    if nj < t:
      dp[i+1][nj] = max(dp[i+1][nj], dp[i][j]+l[i][1])
  now = dp[i][t-1] + l[i][1]
  ans = max(ans, now)
#print(dp)
print(ans)