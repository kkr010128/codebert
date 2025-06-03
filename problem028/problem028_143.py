n,m = map(int,input().split())
coins = list(map(int,input().split()))

inf = float("inf")
dp = [inf]*(n+2)

dp[0]= 0

for i in range(1,n+1):
  for coin in coins:
    if i-coin>=0:
      dp[i]=  min(dp[i-coin]+1,dp[i])
    
print(dp[n])
