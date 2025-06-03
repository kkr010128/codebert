charge, n_coin = map(int,input().split())
coin_ls = list(map(int, input().split()))
coin_ls = [0] + coin_ls

dp = [[float('inf')] * (charge+1) for _ in range(n_coin+1)]
dp[0][0] = 0
for coin_i in range(1,n_coin+1):
    for now_charge in range(0,charge+1):
        if now_charge - coin_ls[coin_i] >= 0:
            dp[coin_i][now_charge] = min(dp[coin_i][now_charge], dp[coin_i][now_charge-coin_ls[coin_i]]+1)
        dp[coin_i][now_charge] = min(dp[coin_i-1][now_charge], dp[coin_i][now_charge]) 
print(dp[n_coin][charge])
