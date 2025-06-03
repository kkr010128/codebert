H, N = map(int,input().split())
ls = [list(map(int,input().split())) for _ in range(N)]

dp = [0]*(H+1)
for i in range(1, H+1):
  for j in range(N):
    if j == 0:
      if ls[j][0] <= i:
        dp[i] = dp[i-ls[j][0]] + ls[j][1]
      else:
        dp[i] = ls[j][1]    
    else:
      if ls[j][0] <= i:
        dp[i] = min([dp[i], dp[i-ls[j][0]] + ls[j][1]])
      else:
        dp[i] = min([dp[i], ls[j][1]])
        
print(dp[H]) 