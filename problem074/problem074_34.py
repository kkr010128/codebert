import numpy as np

N,K = list(map(int, input().split()))
LRs = [list(map(int, input().split())) for _ in range(K)]

dp = np.zeros(N+2, dtype = int)
dp[1] = 1
dp[2] = -1

atai = 0
for i in range(1, N+2):
    atai += dp[i]
    for LR in LRs:
        if(i+LR[0] <= N):
            dp[i+LR[0]] = (dp[i+LR[0]] + atai) % 998244353
        if(i+LR[1] <= N):
            dp[i+LR[1]+1] = (dp[i+LR[1]+1] -atai) % 998244353

#    print(dp)

#復元
ruisekiwa = [0]

for hoge in dp:
    ruisekiwa.append(ruisekiwa[-1]+hoge)
print(ruisekiwa[N+1] % 998244353)