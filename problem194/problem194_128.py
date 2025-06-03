H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

dp = [[10001] * W for _ in range(H)]
if s[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0
moves = [[1, 0],[0, 1]]

for y in range(H):
    for x in range(W):
        for m in moves:
            ny, nx = y+m[0], x+m[1]
            if ny >= H or nx >= W:
                continue
            add = 0
            # .から#に突入する時だけカウントが増える
            if s[y][x] == '.' and s[ny][nx] == '#':
                add = 1
            dp[ny][nx] = min(dp[ny][nx], dp[y][x] + add)
print(dp[-1][-1])
