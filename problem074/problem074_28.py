n, k = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(k)]
dp = [0]*(n+1)
dp[1] = 1
mod = 998244353
dpsum = [0]*(n+1)
dpsum[1] = 1

for i in range(2, n+1):
    for j in range(k):
        li = max(i-s[j][1], 1)
        ri = i-s[j][0]
        if ri < 0:
            continue
        dp[i] += dpsum[ri]-dpsum[li-1]
        dp[i] %= mod
    dpsum[i] = dpsum[i-1]+dp[i]
print(dp[n])
    
