INF = 1e5
n, m = list(map(int, input().split()))
C = list(map(int, input().split()))
dp = [[INF] * (n + 1) for _ in range(m)] 
for i in range(m):
    dp[i][0] = 0
for j in range(1 + n):
    dp[0][j] = j
from itertools import product
for i, j in product(range(1, m), range(1, n + 1)):
    dp[i][j] = min(dp[i][j], dp[i - 1][j])
    if 0 <= j - C[i]:
        dp[i][j] = min(dp[i][j], dp[i][j - C[i]] + 1)

print(dp[i][j])
