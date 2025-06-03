H,W=map(int,input().split())
s=[]
dp=[[10**9]*W for _ in range(H)]
dp[0][0]=0
for _ in range(H):
    s.append(list(input()))
for i in range(H):
    for j in range(W):
        if j!=W-1:
            if s[i][j]=="." and s[i][j+1]=="#":
                dp[i][j+1]=min(dp[i][j]+1,dp[i][j+1])
            else:
                dp[i][j+1]=min(dp[i][j],dp[i][j+1])
        if i!=H-1:
            if s[i][j]=="." and s[i+1][j]=="#":
                dp[i+1][j]=min(dp[i][j]+1,dp[i+1][j])
            else:
                dp[i+1][j]=min(dp[i][j],dp[i+1][j])
ans=dp[H-1][W-1]
if s[0][0]=="#":
    ans+=1
print(ans)