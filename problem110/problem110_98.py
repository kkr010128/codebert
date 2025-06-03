WHITE = '.'
BLACK = '#'

H, W, K = map(int, input().split())
C = [input() for _ in range(H)]

ans = 0
for rows in range(2 ** H):
    for cols in range(2 ** W):
        cnt = 0
        for h in range(H):
            for w in range(W):
                if (rows >> h) & 1 or (cols >> w) & 1:
                    continue
                cnt += C[h][w] == BLACK
        if cnt == K:
            ans += 1
print(ans)