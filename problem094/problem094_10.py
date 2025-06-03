R,C,K = map(int,input().split()) #行、列、個数
G = [[0]*C for _ in range(R)] #G[i][j]でi行目のj番目にある価値
for i in range(K):
  a,b,v = map(int,input().split())
  a-=1;b-=1 #0index
  G[a][b] = v
#print(G)

dp = [[0]*4 for _ in range(C+1)]
#dp[j][k]ある行において、j個目まで見て、その行でk個拾っている
for i in range(R):
  p = [[0]*4 for _ in range(C+1)] #pが前の行、dpが今の行
  p,dp = dp,p
  for j in range(C):
    #print(j+1,dp)
    for k in range(4):
      if k == 0: #その行で一個も取っていなければ上の行から来るだけ
        dp[j+1][k] = max(p[j+1])
      elif k == 1: #一個目をとるということは横からきて取るか、上から来て取るか
        if G[i][j] == 0: #そこにない場合は横から
          dp[j+1][k] = dp[j][k]
        else: #ある場合は横からくるか上から来て一個取るか
          dp[j+1][k] = max(dp[j][k],max(p[j+1])+G[i][j])
      else: #二個以上の場合には上からは来れない。
        if G[i][j] == 0: #そこになければ横からくるだけ
          dp[j+1][k] = dp[j][k]
        else: #あればとったほうがよいか比較
          dp[j+1][k] = max(dp[j][k],dp[j][k-1]+G[i][j])
  #print(p,dp)

ans = max(dp[C])
print(ans)