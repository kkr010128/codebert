c=[[0]*3001for _ in range(3001)]
dp=[[[0]*3001for _ in range(3001)]for _ in range(4)]
h,w,k=map(int,input().split())
for i in range(k):
    y,x,v=map(int,input().split())
    c[y][x]=v
for i in range(1,h+1):
    for j in range(1,w+1):
        x=max(dp[0][i-1][j],dp[1][i-1][j],dp[2][i-1][j],dp[3][i-1][j])
        for k in range(4):
            if k:dp[k][i][j]=max(dp[k][i][j-1],dp[k-1][i][j-1]+c[i][j])
            else:dp[k][i][j]=max(dp[k][i][j-1],x)
        dp[1][i][j]=max(dp[1][i][j],x+c[i][j])
print(max(dp[0][h][w],dp[1][h][w],dp[2][h][w],dp[3][h][w]))