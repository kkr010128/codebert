def resolve():
    H, W, K = map(int, input().split())
    C = [input() for _ in range(H)]
    cnt = 0
    for h in range(1 << H):
        for w in range(1 << W):
            black = 0
            for i in range(H):
                for j in range(W):
                    if h >> i & 1 or w >> j & 1:
                        continue
                    if C[i][j] == "#":
                        black += 1
            if black == K:
                cnt += 1

    print(cnt)
resolve()