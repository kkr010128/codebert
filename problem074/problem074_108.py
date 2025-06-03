n,k = (int(x) for x in input().split())
lr = []
for _ in range(k):
    l,r = (int(x) for x in input().split())
    lr.append((l,r))
lr.sort()

mod = 998244353

dp= [0]*(n+1)
dp[1] = 1

for i in range(2,n+1):
    cnt = 0
    for l,r in lr:
        if l >= i:
            break
        else:
            cnt += dp[i-l] - dp[max(0,i-r-1)]
    dp[i] = (dp[i-1] + cnt) % mod

print(cnt%mod)