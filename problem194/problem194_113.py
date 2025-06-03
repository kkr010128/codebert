h, w = map(int, input().split())
s = [list(map(str, input().rstrip())) for _ in range(h)]

dp = [[10001] * w for _ in range(h)]

if s[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0

moves = [[1, 0], [0, 1]]

for y in range(h):
    for x in range(w):
        for m in moves:
            ny, nx = y + m[0], x + m[1]
            if ny >= h or nx >= w:
                continue
            add = 0
            # .から#に突入する時だけカウントが増える
            if s[y][x] == "." and s[ny][nx] == "#":
                add = 1
            dp[ny][nx] = min(dp[ny][nx], dp[y][x] + add)

print(dp[-1][-1])