def solve():
  R, C, K = map(int, input().split())
  item = [[0]*C for _ in range(R)]
  for i in range(K):
    r,c,v = map(int, input().split())
    item[r-1][c-1] = v
  last_dp = [[0]*(C+1) for _ in range(5)]
  for i in range(1,R+1):
    dp = [[0]*(C+1) for _ in range(5)]
    for j in range(1,C+1):
      for k in range(4): #横から取らない
        dp[k][j] = dp[k][j-1]
      #上から取らない
      dp[0][j] = max(dp[0][j],last_dp[-1][j])
      if item[i-1][j-1]>0:
        #上からとる
        dp[1][j] = max(dp[1][j],last_dp[-1][j]+item[i-1][j-1])
        for k in range(1,4): #横から取る
          dp[k][j] = max(dp[k][j],dp[k-1][j-1]+item[i-1][j-1])
      for k in range(4):
        dp[-1][j] = max(dp[-1][j],dp[k][j])
    last_dp = dp
  ans = last_dp[-1][-1]
  return ans
print(solve())