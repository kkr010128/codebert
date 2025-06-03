N=[int(c) for c in input()][::-1]

dp=[[0]*2 for _ in range(len(N)+1)]
dp[0][1]=1

for i in range(len(N)):
    dp[i+1][1]=min(dp[i][0]+N[i]+1,dp[i][1]+10-N[i]-1)
    dp[i+1][0]=min(dp[i][0]+N[i],dp[i][1]+10-N[i])

print(dp[len(N)][0])