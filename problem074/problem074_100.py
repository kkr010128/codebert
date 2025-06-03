N, k = map(int, input().split())

dp = [0] * (N+1)
dp[1] = 1

S = []
for i in range(k):
    S.append(list(map(int, input().split())))

for i in range(2, N+1):
    for l, r in S:
        dp[i] += (dp[max(i-l, 0)] - dp[max(i-r-1, 0)])
    dp[i] += dp[i-1]
    dp[i] %= 998244353
print((dp[N] - dp[N-1])%998244353)