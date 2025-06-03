N, K = map(int, input().split())
MOD = 998244353
S = []
for _ in range(K):
    S.append(tuple(map(int, input().split())))

dp = [0] * (N + 1)
dp[1] = 1
sum_list = [0] * (N + 1)
sum_list[1] = 1

for i in range(2, N+1):
    for L, R in S:
        RR = i - L
        if RR <= 0:
            continue
        LL = max(1, i-R)
        if LL <= RR:
            t = sum_list[RR] - sum_list[LL-1]
            dp[i] += t
            dp[i] %= MOD
    sum_list[i] = (sum_list[i-1] + dp[i]) % MOD

print(dp[N])
