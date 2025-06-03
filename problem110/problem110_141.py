H, W, K = map(int, input().split())

c = []
b_h = [0] * H
b_w = [0] * W
b = 0

for h in range(H):
    c.append(input().rstrip())
    for w in range(W):
        if c[h][w] == "#":
            b_h[h] += 1
            b_w[w] += 1
            b += 1

ans = 0
for hi in range(2 ** H):
    for wi in range(2 ** W):
        bsum = b

        for h in range(H):
            if hi & (2 ** h) != 0:
                bsum -= b_h[h]
                for w in range(W):
                    if wi & 2 ** w != 0:
                        if c[h][w] == '#':
                            bsum += 1

        for w in range(W):
            if wi & (2 ** w) != 0:
                bsum -= b_w[w]

        if bsum == K:
            ans += 1

print(ans)
