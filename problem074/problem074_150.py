MOD = 998244353
N, K = map(int, input().split())
rl = [list(map(int, input().split())) for _ in range(K)]
dp = [0] * (N + 1)
sdp = [0] * (N + 1)
dp[1] = 1
sdp[1] = 1

for i in range(2, N + 1):
    for j in range(K):
        l, r = rl[j][0], rl[j][1]
        tl = max(1, i - r)
        tr = max(0, i - l)
        dp[i] += sdp[tr] - sdp[tl - 1]
        dp[i] %= MOD
    sdp[i] += dp[i] + sdp[i - 1]
    sdp[i] %= MOD

print(dp[N])