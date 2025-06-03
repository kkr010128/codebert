S = input()[::-1]
l = len(S)
dp = [[0]*2 for _ in range(l+1)]
dp[1][0]=dp[0][0]+int(S[0])
dp[1][1]=dp[0][1]+10-int(S[0])
for i in range(1,l):
  dp[i+1][0]=min(dp[i][0]+int(S[i]),dp[i][1]+int(S[i])+1)
  dp[i+1][1]=min(dp[i][0]+10-int(S[i]),dp[i][1]+10-int(S[i])-1)
  
print(min(dp[-1][0],dp[-1][1]+1))