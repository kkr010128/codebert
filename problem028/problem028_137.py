n,m = map(int,input().split())
coins = sorted(list(map(int,input().split())),reverse=True)

dp = [float("inf")]*50001

dp[0] = 0

for  i in range(50001):
    for coin in coins:
        if i+coin > 50000:
            continue
        
        else:
            dp[i+coin] = min(dp[i+coin], dp[i]+1)

print(dp[n])
