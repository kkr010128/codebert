import sys

readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

H, W = map(int, readline().split())
masu = []
for _ in range(H):
    masu.append(readline().rstrip().decode('utf-8'))
# print(masu)

dp = [[INF]*W for _ in range(H)]
dp[0][0] = int(masu[0][0] == "#")

dd = [(1, 0), (0, 1)]

# 配るDP
for i in range(H):
    for j in range(W):
        for dx, dy in dd:
            ni = i + dy
            nj = j + dx
            # はみ出す場合
            if (ni >= H or nj >= W):
                continue
            add = 0
            if masu[ni][nj] == "#" and masu[i][j] == ".":
                add = 1
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + add)
# print(dp)
ans = dp[H-1][W-1]
print(ans)