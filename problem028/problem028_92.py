n,m=map(int,input().split())
c=list(map(int,input().split()))
dp=[[10001]*m for i in range(n)] #dp[value][i_coin]
dp.insert(0,[0]*m)
for i in range(m):
  for v in range(1,n+1):
    if i==0:
      dp[v][i]=v//c[i] if v%c[i]==0 else 10001
      continue
    if v<c[i]:
        dp[v][i]=dp[v][i-1]
    else:
      dp[v][i]=min(dp[v][i-1],dp[v-c[i]][i]+1)
print(dp[n][m-1])
