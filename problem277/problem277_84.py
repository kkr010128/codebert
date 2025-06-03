H, W, K = map(int, input().split())
grid = [input() for _ in range(H)]
ans = [[0] * W for _ in range(H)]

cnt = 1
for h in range(H):
    for w in range(W):
        if grid[h][w] == "#":
            ans[h][w] = cnt
            cnt += 1

# left -> right
for h in range(H):
    for w in range(1, W):
        if ans[h][w] == 0 and ans[h][w - 1] != 0:
            ans[h][w] = ans[h][w - 1]

# right -> left
for h in range(H):
    for w in range(W - 2, -1, -1):
        if ans[h][w] == 0 and ans[h][w + 1] != 0:
            ans[h][w] = ans[h][w + 1]

# top -> bottom
for h in range(1, H):
    for w in range(W):
        if ans[h][w] == 0 and ans[h - 1][w] != 0:
            ans[h][w] = ans[h - 1][w]

# bottom -> top
for h in range(H - 2, -1, -1):
    for w in range(W):
        if ans[h][w] == 0 and ans[h + 1][w] != 0:
            ans[h][w] = ans[h + 1][w]

for a in ans:
    print(*a)
