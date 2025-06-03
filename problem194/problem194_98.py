import collections
H, W, *S = open(0).read().split()
H, W = [int(_) for _ in [H, W]]
dist = [[float('inf')] * W for _ in range(H)]
dist[0][0] = 0
Q = collections.deque([0])
while True:
    if not Q:
        break
    i = Q.popleft()
    x, y = divmod(i, W)
    d = dist[x][y]
    for dx, dy in ((1, 0), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W:
            if S[nx][ny] == '#' and S[x][y] == '.':
                if dist[nx][ny] > d + 1:
                    dist[nx][ny] = d + 1
                    Q += [nx * W + ny]
            elif dist[nx][ny] > d:
                dist[nx][ny] = d
                Q += [nx * W + ny]
ans = dist[-1][-1]
if S[0][0] == '#':
    ans += 1
print(ans)
