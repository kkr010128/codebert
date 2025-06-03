import sys
H, W, K = map(int, sys.stdin.readline().rstrip().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(H)]

ans = [[-1] * W for _ in range(H)] 
color = 0
for h in range(H):
    flag = False
    color += 1
    for w in range(W):
        if grid[h][w] == "#":
            if not flag:
                flag = True
            else:
                color += 1
        ans[h][w] = color
    if not flag:
        for w in range(W):
            ans[h][w] = -1
        color -= 1

for w in range(W):
    idx = []
    color = -1
    for h in range(H):
        if ans[h][w] == -1:
            if color != -1:
                ans[h][w] = color
            else:
                idx.append(h)
        else:
            color = ans[h][w]
            if idx:
                for i in idx:
                    ans[i][w] = color
                idx = []

for a in ans:
    print(" ".join(map(str, a)))