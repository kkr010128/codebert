def solve(l, r, i):
    if i - l < 1:
        return 0
    return dp[i - l] - dp[max(i - r - 1, 0)]


n, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(k)]
MOD = 998244353

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    tmp = 0
    for l, r in lr:
        tmp += solve(l, r, i)
    tmp = tmp % MOD
    dp[i] = (dp[i - 1] + tmp) % MOD

print(tmp)