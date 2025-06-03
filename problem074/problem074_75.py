n,k = map(int,input().split())
mod = 998244353
dp = [0]*(n+10)
dpsum = [0]*(n+10)
dp[1] = dpsum[1] = 1
L = [0]*k
R = [0]*k
for i in range(k):
    l,r = map(int,input().split())
    L[i],R[i] = l,r
for i in range(2,n+1):
    for j in range(k):
        li = i-R[j]
        ri = i-L[j]
        if ri < 0: continue
        li = max(li,1)
        dp[i] += dpsum[ri]-dpsum[li-1]
        dp[i] %= mod
    dpsum[i] = dpsum[i-1]+dp[i]
    dpsum[i] %= mod
print(dp[n])