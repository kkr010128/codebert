INF=10**30
N=list(map(int,list(input())))[::-1]
l=len(N)
dp=[[INF,INF] for i in range(l+1)]
dp[0][0]=0
for i in range(l):
    dp[i+1][0]=min(dp[i][0]+N[i],dp[i][1]+N[i]+1)
    dp[i+1][1]=min(dp[i][0]+(10-N[i]),dp[i][1]+(9-N[i]))
print(min(dp[l][0],dp[l][1]+1))