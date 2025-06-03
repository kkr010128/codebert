H, W, K = map(int, input().split())
grid = 'x' * (W + 2)
for _ in range(H):
    grid += 'x' + input() + 'x'
grid += 'x' * (W + 2)

N = len(grid)
strb = [i for i in range(N) if grid[i] == '#']
G = [0] * N

for i, s in enumerate(strb, 1):
    q = [s]
    while q:
        x = q.pop()
        if G[x] != 0:
            continue
        G[x] = i
        for dx in [1, -1]:
            y = x + dx
            if grid[y] == '.' and G[y] == 0:
                q.append(y)

for i in range(N - 1, -1, -1):
    if G[i] == 0 and i + W + 2 < N:
        G[i] = G[i + W + 2]

for i in range(N):
    if G[i] == 0 and i - W - 2 < N:
        G[i] = G[i - W - 2]

j = 0
for i in range(H):
    print(' '.join(str(x) for x in G[j + W + 3:j + 2 * W + 3]))
    j += W + 2
