n,t=map(int,input().split())
dp=[[-1 for j in range(2)] for i in range(t+1)]
dp[0][0]=0
d=[]
for i in range(n):
    d.append(list(map(int,input().split())))
d.sort()
for i in range(n):
    for j in range(t,-1,-1):
        for k in range(1,-1,-1):
            if k==0:
                if dp[j][k]>=0 and j+d[i][0]<t:
                    dp[j+d[i][0]][k]=max(dp[j+d[i][0]][k],dp[j][k]+d[i][1])
            if k==1:
                if dp[j][0]>=0:
                    dp[j][k]=max(dp[j][k],dp[j][0]+d[i][1])
ans=0
for i in range(t+1):
    for j in range(2):
        ans=max(ans,dp[i][j])
print(ans)
