# 解説見た
n,k = map(int,input().split())
lr = [list(map(int,input().split())) for _ in range(k)]
dp = [0]*(n+1)
sdp = [0]*(n+1)
dp[1],sdp[1] = 1,1
mod = 998244353

for i in range(1,n+1):
    for l,r in lr:
        if i-l<0:
            continue
        else:
            dp[i] += sdp[i-l] - sdp[max(0,i-r-1)]
    sdp[i] = sdp[i-1] + dp[i]
    dp[i] %= mod
    sdp[i] %= mod
    
print(dp[-1])