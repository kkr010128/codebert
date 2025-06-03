s = int(input())
#最後に切った場所がiであるようなパターンの数をdp[i]とする
dp=[0]*(s+1)
dp[0]=1
if s<3:
  print("0")  
else:
  for i in range(3,s+1):
    dp[i]=dp[i-1]+dp[i-3]
    dp.append(dp[i])
    score=dp[s]%(10**9+7)
  print(score)