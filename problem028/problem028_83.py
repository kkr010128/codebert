n,m  = map(int,input().split())

coins = list(map(int,input().split()))

dp = [20**10]*(n+1)
dp[0] = 0
for coin in coins:
    for price in range(coin,n+1):
        dp[price]  = min(dp[price],dp[price-coin]+1)
        
print(dp[n])
