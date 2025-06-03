n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()

dp=[[0]*3 for i in range(n+1)]

for i in range(n):
    if t[i]=='r':
      dp[i+1][2]=max(dp[i+1-k][0],dp[i+1-k][1])+p
      dp[i+1][1]=max(dp[i+1-k][0],dp[i+1-k][2])
      dp[i+1][0]=max(dp[i+1-k][1],dp[i+1-k][2])
    

    elif t[i]=='s':
      dp[i+1][0]=max(dp[i+1-k][1],dp[i+1-k][2])+r
      dp[i+1][1]=max(dp[i+1-k][0],dp[i+1-k][2])
      dp[i+1][2]=max(dp[i+1-k][0],dp[i+1-k][1])
      
      
    else:
      dp[i+1][1]=max(dp[i+1-k][0],dp[i+1-k][2])+s
      dp[i+1][0]=max(dp[i+1-k][1],dp[i+1-k][2])
      dp[i+1][2]=max(dp[i+1-k][0],dp[i+1-k][1])
      


ans=0

for i in range(1,k+1):
  ans+=max(dp[-i])


print(ans)