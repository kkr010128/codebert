R,C,K=map(int,input().split())
point=[[0]*C for _ in range(R)]
for _ in range(K):
    r,c,v=map(int,input().split())
    point[r-1][c-1]=v

dp=[[[0]*C for _ in range(R)] for _ in range(4)]
dp[1][0][0]=point[0][0]
for i in range(R):
    for j in range(C-1):
        for k in range(4):
            dp[k][i][j+1]=max(dp[k][i][j+1],dp[k][i][j])
            if k!=0:
                dp[k][i][j+1]=max(dp[k][i][j+1],dp[k-1][i][j]+point[i][j+1])
    if i==R-1:
        break
    for j in range(C):
        mx=0
        for k in range(4):
            mx=max(dp[k][i][j],mx)
        dp[0][i+1][j]=mx
        dp[1][i+1][j]=mx+point[i+1][j]
ans=0
for i in range(4):
    ans=max(ans,dp[i][R-1][C-1])
print(ans)