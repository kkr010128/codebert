H, W, K = map(int, input().split())
M = [[1 if c == "#" else 0 for c in input()] for _ in range(H)]

ans = 0
for hselection in range(1 << H):
    for wselection in range(1 << W):
        count = 0
        for h in range(H):
            if hselection & (1 << h):
                continue
            for w in range(W):
                if wselection & (1 << w):
                    continue
                count += M[h][w]
        if count == K:
            ans += 1
print(ans)