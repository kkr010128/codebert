N = list(map(int, list(input())))

dp=[[-1,-1] for i in range(len(N)+1)]
dp[0]=[0,1]
b=0
N.insert(0,0)

for i in range(1,len(N)):
    up = 10-N[i]
    dp[i][0]=min(dp[i-1][0]+N[i],dp[i-1][1]+up)
    dp[i][1] = min(dp[i-1][0]+N[i]+1, dp[i-1][1]+up-1)
   

print(dp[-1][0])
