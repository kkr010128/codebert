N, M = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]

dp = [50001] * (N + 1)
dp[0] = 0

for c in C:
    for n in range(c, N + 1):
        dp[n] = min(dp[n], dp[n - c] + 1)

print(dp[-1])
