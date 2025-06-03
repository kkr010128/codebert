H, W, k = map(int, input().split())
a = [list(input()) for _ in range(H)]
res = [[0] * W for _ in range(H)]
cnt = 0
for h in range(H):
    for w in range(W):
        if a[h][w] == "#":
            cnt += 1
            res[h][w] = cnt

for h in range(H):
    for w in range(W):
        if w > 0 and res[h][w] == 0:
            res[h][w] = res[h][w - 1]

for h in range(H):
    for w in reversed(range(W)):
        if w < W - 1 and res[h][w] == 0:
            res[h][w] = res[h][w + 1]

for h in range(H):
    for w in range(W):
        if h > 0 and res[h][w] == 0:
            res[h][w] = res[h - 1][w]

for h in reversed(range(H)):
    for w in range(W):
        if h < H - 1 and res[h][w] == 0:
            res[h][w] = res[h + 1][w]

for i in res:
    print(*i)
