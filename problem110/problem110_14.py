H, W, K = map(int, input().split())
C = ["" for _ in range(H)]
for h in range(H):
    C[h] = [s for s in input()]

cnt = 0
for h in range(1 << H):
    for w in range(1 << W):
        black = 0
        for i in range(H):
            if (h >> i & 1) == 1:
                continue
            for j in range(W):
                if (w >> j & 1) == 1:
                    continue
                if C[i][j] == "#":
                    black += 1
        if black == K:
            cnt += 1
print(cnt)
