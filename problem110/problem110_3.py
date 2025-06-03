H, W, K = map(int, input().split())
C = [[(c=="#") for c in input()] for _ in range(H)]
cnt0 = sum(sum(c) for c in C)
ans = 0
for sy in range(1<<H):
    for sx in range(1<<W):
        D = [c.copy() for c in C]
        cnt = cnt0
        for y in range(H):
            for x in range(W):
                if sy>>y&1 | sx>>x&1:
                    cnt -= D[y][x]
                    D[y][x] = False
        if cnt == K:
            ans += 1
print(ans)
