from sys import stdin
readline = stdin.readline

payment, _ = map(int, readline().split())
coin = list(map(int, readline().split()))

dp = [float('inf')] * (payment + 1)
dp[0] = 0

for ci in coin:
    for pi in range(ci, len(dp)):
        if dp[pi] > dp[pi - ci] + 1:
            dp[pi] = dp[pi - ci] + 1
print(dp[-1])