mod = 998244353
n,k = map(int,input().split())
lr = [[int(i) for i in input().split()] for j in range(k)]

dp = [0]*(n+1)
dp_rui = [0]*(n+1)

dp[1] = 1
dp_rui[1] = 1

for i in range(2,n+1):
    for j in range(k):
        lft = i - lr[j][1]
        rht = i - lr[j][0]
        #print(i,lft,rht)
        if rht <= 0:
            continue
        lft = max(1,lft)
        dp[i] += dp_rui[rht] - dp_rui[lft-1]
        #print(dp_rui[rht],dp_rui[lft-1])
        dp[i] %= mod
        #print(dp)
        #print(dp_rui)
    dp_rui[i] = dp_rui[i-1] + dp[i]
    dp_rui[i] %= mod

print(dp[n]%mod)