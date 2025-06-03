h,w = map(int, input().split())
s = [input()+"." for i in range(h)] + ["."*(w+1)]
INF = 10 ** 18
dp = [[INF]*(w+1) for i in range(h+1)]
dp[0][0] = 1 if s[0][0] == "#" else 0
for i in range(h):
  for j in range(w):
    if s[i][j] == "#":
      dp[i+1][j] = min(dp[i+1][j], dp[i][j])
      dp[i][j+1] = min(dp[i][j+1], dp[i][j])
    else:
      vi = 1 if s[i+1][j] == "#" else 0
      vj = 1 if s[i][j+1] == "#" else 0
      dp[i+1][j] = min(dp[i+1][j], dp[i][j]+vi)
      dp[i][j+1] = min(dp[i][j+1], dp[i][j]+vj)
print(dp[h-1][w-1])