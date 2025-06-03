import sys

n, m = map(int, sys.stdin.readline().strip().split())
c = list(map(int, sys.stdin.readline().strip().split()))

dp = [float("inf") for _ in range(n+1)]
dp[0] = 0

for i in range(n+1):
    for c_i in c:
        if i - c_i >= 0:
            dp[i] = min(dp[i], dp[i - c_i] + 1)

print(dp[n])
