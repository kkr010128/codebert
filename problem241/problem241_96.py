h, w = map(int, input().split())
s = [input() for _ in range(h)]

def bfs(x, y):
    q = []
    dp = {}
    def qpush(x, y, t):
        if 0 <= x < w and 0 <= y < h and s[y][x] != '#' and (x, y) not in dp:
            q.append((x, y))
            dp[(x, y)] = t

    qpush(x, y, 0)
    while len(q) > 0:
        (x, y) = q.pop(0)
        qpush(x + 1, y, dp[(x, y)] + 1)
        qpush(x, y - 1, dp[(x, y)] + 1)
        qpush(x - 1, y, dp[(x, y)] + 1)
        qpush(x, y + 1, dp[(x, y)] + 1)
    return dp.get((x, y), 0)

t = 0
for y in range(h):
    for x in range(w):
        t = max(t, bfs(x, y))
print(t)