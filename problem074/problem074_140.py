N, K = (int(i) for i in input().split())
l, r = [0]*K, [0]*K
for k in range(K):
    l[k], r[k] = (int(x) for x in input().split())

# dp : マスiまで移動する方法のパターン数
# TLE
'''
import numpy as np
dp = [0]*N
dp[0] = 1
for i in range(N):
    for k in range(K):
        for j in range(l[k], r[k]+1):
            if (i+j < N):
                dp[i+j] = dp[i+j] + dp[i]
            if j == r[k]:
                print(i, (l[k], r[k]), dp, np.diff(dp))
print(dp[-1]%998244353)
'''

# dp : マスiまで移動する方法のパターン数
# dps : dp[i] と dp[i+1] の 差
dp = [0]*N
dps = [0]*(N-1)
dp[0] = 1
dps[0] = -1
for i in range(N-1):
    for k in range(K):
        if i + l[k] - 1 < (N - 1):
            dps[i + l[k] - 1] += dp[i]
        if i + r[k] < (N - 1):
            dps[i + r[k]    ] -= dp[i]
        #print(i, (l[k], r[k]), dp, dps)
    dp[i+1] = (dps[i] + dp[i])%998244353
print(dp[-1]%998244353)