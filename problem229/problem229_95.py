h,n=map(int,input().split())
ab=[[] for i in range(n)]
for i in range(n):
  ab[i]=list(map(int,input().split()))
  
dp=[100000000 for i in range(h+1)]
dp[0]=0
for hi in range(h):
  for i in range(n):
    damage=min(h,hi+ab[i][0])
    dp[damage] = min(dp[damage],dp[hi]+ab[i][1])
    #print(damage,dp[damage],dp[hi]+ab[i][1])
print(dp[h])