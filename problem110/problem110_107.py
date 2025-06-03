H, W, K = map(int, input().split())

blacks = [[None] * W for _ in range(H)]
black_sums = [[0] * W for _ in range(H)]
black_col_sums = [[0] * W for _ in range(H)]

for i in range(H):
    for j, item in enumerate(input()):
        if item == "#":
            blacks[i][j] = 1
        else:
            blacks[i][j] = 0


ok_count = 0
for i in range(1<<H):
    for j in range(1<<W):
        # print(f"{i:b}, {j:b}")

        black_count = 0
        for m in range(H):
            for n in range(W):
                if (1 & i >> m and 1 & j >> n) == False:
                    continue
                black_count += blacks[m][n]
        if black_count == K:
            ok_count += 1

print(ok_count)