
import sys

inf_val = 10**10

m, n = map(int, sys.stdin.readline().split())
numbers = map(int, sys.stdin.readline().split())

dp = [inf_val]*(m+1)
dp[0] = 0

for x in numbers:
    for y in xrange(x, m+1):
        dp[y] =  min(dp[y-x]+1, dp[y])

print dp[m]