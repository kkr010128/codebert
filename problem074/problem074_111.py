n, k = map(int, input().split())
s = [] 
mod = 998244353

for i in range(k):
    l, r = map(int, input().split())
    s.append([l, r])

dp = [0 for _ in range(n+1)]
dp[1] = 1
dpsum = [0 for _ in range(n+1)]
dpsum[1] = 1

for i in range(2,n+1):
    for l, r in s:
        li = max(i-r,1)
        ri = max(i-l,0)
        dp[i] += (dpsum[ri] - dpsum[li-1])%mod
    dpsum[i] = (dpsum[i-1] + dp[i])%mod

print(dp[n]%mod)