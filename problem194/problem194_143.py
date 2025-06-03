H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append([c for c in input()])

cnts = [[0 for _ in range(W)] for _ in range(H)]
if S[0][0] == "#":
    cnts[0][0]  = 1
for h in range(H):
    for w in range(W):
        if h == 0 and w == 0:
            continue

        c1, c2 = float('inf'), float('inf')
        if 0 <= h - 1:
            c1 = cnts[h - 1][w]
            if S[h][w] == "#" and S[h - 1][w] == ".":
                c1 += 1

        if 0 <= w - 1:
            c2 = cnts[h][w - 1]
            if S[h][w] == "#" and S[h][w - 1] == ".":
                c2 += 1

        cnts[h][w] = min(c1, c2)
print(cnts[H-1][W-1])
