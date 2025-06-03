H, N = map(int, input().split())
dp = [10 ** 9] * (H + 1)
dp[0] = 0
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(H):
        idx = min(H, i + a)
        dp[idx] = min(dp[idx], dp[i] + b)
print(dp[H])

