import sys
input = sys.stdin.buffer.readline
H, N = map(int, input().split())
A = [tuple(map(int, line.split())) for line in sys.stdin.buffer.readlines()]
INF = 1 << 30
dp = [INF]*(H+1)
dp[H] = 0
for i in range(N):
    a, b = A[i]
    for h in range(H, -1, -1):
        x = h-a if h-a > 0 else 0
        if dp[x] > dp[h]+b:
            dp[x] = dp[h]+b
print(dp[0])
