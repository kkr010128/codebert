N, M = map(int, input().split())
c = list(map(int, input().split()))

dp = [0] + [float('inf')] * N
for m in range(M):
    ci = c[m]
    for n in range(N + 1):
        if n - ci >= 0:
            dp[n] = min(dp[n], dp[n - ci] + 1)

print(dp[N])
