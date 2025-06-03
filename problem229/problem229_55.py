import sys
input = sys.stdin.buffer.readline
H, N = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
dp = [10**9] * (H + 1)
dp[0] = 0
for i in range(H + 1):
    for a, b in ab:
        if i - a < 0:
            dp[i] = min(dp[i], b)
        else:
            dp[i] = min(dp[i], dp[i - a] + b)
print(dp[H])
