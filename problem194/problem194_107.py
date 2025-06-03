H, W = map(int, input().split())
s = [input() for _ in range(H)]
dp = [[float('inf') for _ in range(W)] for _ in range(H)]
if s[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0
dx = [0, 1]
dy = [1, 0]

for i in range(H):
    for j in range(W):
        for k in range(2):
            ni = i + dx[k]
            nj = j + dy[k]
            if ni >= H or nj >= W:
                continue
            add = 0
            # print(i, j, ni, nj)
            if s[i][j] == '.' and s[ni][nj] == '#': add += 1
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + add)

            # print(dp)
print(dp[H-1][W-1])