h, w = map(int, input().split())
M = [list(input()) for _ in range(h)]
count = [[int(1e18) for _ in range(w)] for _ in range(h)]
count[0][0] = 1 if M[0][0] == '#' else 0

# 同じ色かどうかを見る
for i in range(h):
    for j in range(w):
        if i + 1 < h:
            v = 1 if M[i][j] != M[i + 1][j] else 0
            count[i + 1][j] = min(count[i + 1][j], count[i][j] + v)
        if j + 1 < w:
            v = 1 if M[i][j] != M[i][j + 1] else 0
            count[i][j + 1] = min(count[i][j + 1], count[i][j] + v)

print((count[h - 1][w - 1] + 1) // 2)