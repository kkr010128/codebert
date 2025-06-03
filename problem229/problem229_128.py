h,n=map(int,input().split())
INF=10**18
dp=[INF]*(h+1)
dp[0]=0
for _ in range(n):
  a,b=map(int,input().split())
  for i in range(h+1):
    dp[min(i+a,h)]=min(dp[min(i+a,h)],dp[i]+b)
print(dp[h])