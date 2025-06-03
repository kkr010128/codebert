def solve():
  R, C, K = map(int, input().split())
  item = [[0]*C for _ in range(R)]
  for i in range(K):
    r,c,v = map(int, input().split())
    item[r-1][c-1] = v
  last_dp = [[0]*5 for _ in range(C+1)]
  for i in range(1,R+1):
    dp = [[0]*5 for _ in range(C+1)]
    for j in range(1,C+1):
      for k in range(4): #横から取らない
        dp[j][k] = dp[j-1][k]
      #上から取らない
      dp[j][0] = max(dp[j][0],last_dp[j][-1])
      if item[i-1][j-1]>0:
        #上からとる
        dp[j][1] = max(dp[j][1],last_dp[j][-1]+item[i-1][j-1])
        for k in range(1,4): #横から取る
          dp[j][k] = max(dp[j][k],dp[j-1][k-1]+item[i-1][j-1])
      dp[j][4] = max(dp[j][:4])
    last_dp = dp
  ans = max(last_dp[-1])
  return ans
print(solve())