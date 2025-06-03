from collections import defaultdict
import sys


def input(): return sys.stdin.readline().rstrip()


r, c, K = map(int, input().split())

dp = [[[0]*(c+1) for _ in range(r+1)] for i in range(4)]

# dp[N][i][j] := (i,j) にN個目でたどりつく方法
d = [[0 for i in range(c+1)] for j in range(r+1)]

for _ in range(K):
    r_, c_, v = map(int, input().split())
    d[r_][c_] = v
for i in range(1, r+1):
    for j in range(1, c+1):
        v = d[i][j]
        if v > 0:
            maxi = max(dp[k][i-1][j] for k in range(4))
            dp[0][i][j] = max(maxi, dp[0][i][j-1])
            dp[1][i][j] = max(dp[1][i][j-1], dp[0][i][j-1]+v, maxi+v)
            dp[2][i][j] = max(dp[2][i][j-1], dp[1][i][j-1]+v)
            dp[3][i][j] = max(dp[3][i][j-1], dp[2][i][j-1]+v)

        elif v == 0:
            maxi = max(dp[k][i-1][j] for k in range(4))
            dp[0][i][j] = max(dp[0][i][j-1], maxi)
            dp[1][i][j] = dp[1][i][j-1]
            dp[2][i][j] = dp[2][i][j-1]
            dp[3][i][j] = dp[3][i][j-1]


ans = max(dp[k][r][c] for k in range(4))

print(ans)