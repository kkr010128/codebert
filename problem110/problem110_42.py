def resolve():
    H, W, K = map(int, input().split())

    c = [list(input()) for _ in range(H)]
    ans = 0

    for i in range(2**H):

        for j in range(2**W):

            now = 0
            for x in range(H):
                for y in range(W):

                    if 2**x & i > 0 and 2**y & j > 0:
                        if c[x][y] == "#":
                            now += 1

            if now == K:
                ans += 1

    print(ans)


resolve()