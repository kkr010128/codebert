import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

H,W = map(int,readline().split())
s = [readline().rstrip() for i in range(H)]

dp = [[INF] * W for i in range(H)]

dp[0][0] = 0 if s[0][0] == '.' else 1

for i in range(H):
    ii = max(0,i-1)
    for j in range(W):
        jj = max(0,j-1)
        dp[i][j] = min(dp[ii][j] + (s[i][j] != s[ii][j]), dp[i][jj] + (s[i][j] != s[i][jj]))

print((dp[H-1][W-1]+1)//2)
