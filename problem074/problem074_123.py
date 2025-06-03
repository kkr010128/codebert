#もらうDPで考える
N, K = map(int, input().split())

l = []
r = []

MOD = 998244353

for i in range(K):
    a,b = map(int, input().split())
    l.append(a)
    r.append(b)

dp = [0] * (N+1)
#スタート地点が1なので、dp[1]を1とする
dp[1] = 1

dpsum = [0] * (N+1)
dpsum[1] = 1

for i in range(2, N+1):
    for j in range(K):
        #[l[i], r[i]]
        li = i - r[j]
        ri = i - l[j]
        if ri < 0: continue
        # l1が負になるケースをハンドリング
        li = max(1, li)
        dp[i] += (dpsum[ri] - dpsum[li-1])%MOD #dp[li] ~ dp[ri]の和を足す
    dpsum[i] = (dpsum[i-1] + dp[i])%MOD

print(dp[N]%MOD)