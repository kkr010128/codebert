import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

R, C, K = mapint()
dp = [[[0]*C for _ in range(R)] for _ in range(4)]
from collections import defaultdict
dic = [[0]*C for _ in range(R)]
for _ in range(K):
    r, c, v = mapint()
    dic[r-1][c-1] = v

for r in range(R):
    for c in range(C):
        v = dic[r][c]
        for i in range(4):
            if c!=0:
                dp[i][r][c] = dp[i][r][c-1]
            if r!=0:
                dp[0][r][c] = max(dp[0][r][c], dp[i][r-1][c])
        for i in range(2, -1, -1):
            dp[i+1][r][c] = max(dp[i+1][r][c], dp[i][r][c]+v)

ans = 0
for i in range(4):
    ans = max(ans, dp[i][R-1][C-1])
print(ans)
