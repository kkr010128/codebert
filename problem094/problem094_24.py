from sys import stdin
input = stdin.readline

r, c, k = map(int, input().split())
vals = [[0]*c for _ in range(r)]
for _ in range(k):
    x, y, v = map(int, input().split())
    vals[x-1][y-1] = v
dp = [[0]*4 for j in range(c)]
for j in range(c):
    if j > 0:
        for k in range(4):
            dp[j][k] = dp[j-1][k]
    if vals[0][j] > 0:
        for k in reversed(range(3)):
            if dp[j][k+1] < dp[j][k] + vals[0][j]:
                dp[j][k+1] = dp[j][k] + vals[0][j]
for i in range(1, r):
    tmp = [[max(dp[j]), 0, 0, 0] for j in range(c)]
    for j in range(c):
        if j > 0:
            for k in range(4):
                if tmp[j][k] < tmp[j-1][k]:
                    tmp[j][k] = tmp[j-1][k]
        if vals[i][j] > 0:
            for k in reversed(range(3)):
                if tmp[j][k+1] < tmp[j][k] + vals[i][j]:
                    tmp[j][k+1] = tmp[j][k] + vals[i][j]
    dp = tmp
print(max(dp[-1]))