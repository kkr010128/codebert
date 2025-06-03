R, C, K = map(int, input().split())

Items = [[0] * (C + 1) for _ in range(R + 1)]
for _ in range(K):
    r, c, v = map(int, input().split())
    Items[r][c] = v


DP = [[0] * 4 for _ in range(R + 1)]

for x in range(1, C+1):
    for y in range(1, R+1):
        v = Items[y][x]
        if v:
            DP[y][3] = max(DP[y][3], DP[y][2] + v)
            DP[y][2] = max(DP[y][2], DP[y][1] + v)
            DP[y][1] = max(max(DP[y][1], DP[y][0] + v), max(DP[y-1]) + v)
            DP[y][0] = max(DP[y][0], max(DP[y-1]))
        else:
            DP[y][0] = max(DP[y][0], max(DP[y-1]))

print(max(DP[R]))