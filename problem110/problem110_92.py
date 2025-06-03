H, W, K = map(int,input().split())
grid = [list(input()) for i in range(H)]
total = 0
for mask1 in range(1<<H):
    for mask2 in range(1<<W):
        ct = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j]=='#' and not (1<<i)&mask1 and not (1<<j)&mask2:
                    ct += 1
        if ct==K:
            total += 1
print(total)