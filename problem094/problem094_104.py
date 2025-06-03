import sys
from itertools import product
input = lambda:sys.stdin.buffer.readline().rstrip()

m, n, k = map(int, input().split())
grid = [[0] * n for _ in range(m)]
for _ in range(k):
    i, j, v = map(int, input().split())
    i -= 1; j -= 1
    grid[i][j] = v

dp = [[0] * 4 for _ in range(n)]
for i in range(m):
    ndp = [[0] * 4 for _ in range(n)]
    for j, k in product(range(n), range(4)):
        # from top
        ndp[j][0] = max(ndp[j][0], dp[j][k])
        ndp[j][1] = max(ndp[j][1], dp[j][k] + grid[i][j])
        # from left
        if j > 0:
            ndp[j][k] = max(ndp[j][k], ndp[j - 1][k])
            if k > 0:
                ndp[j][k] = max(ndp[j][k], ndp[j - 1][k - 1] + grid[i][j])
    dp = ndp

print(max(dp[-1]))