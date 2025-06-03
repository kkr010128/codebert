h, w = map(int, input().split())
ma = [ list(input()) for _ in range(h) ]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0

def bfs(sy, sx):
    if ma[sy][sx] == "#":
        return 0
    q = [[sy, sx, 0]]
    flag = [[0] * w for _ in range(h)]
    flag[sy][sx] = 1
    ans = 0
    while True:
        if len(q) == 0:
            break
        y, x, dist = q.pop(0)
        for dy, dx in d:
            if 0 <= y + dy < h and 0 <= x + dx < w and flag[y + dy][x + dx] == 0 and ma[y + dy][x + dx] == ".":
                flag[y + dy][x + dx] = 1
                q.append([y + dy, x + dx, dist + 1])
                ans = max(ans, dist + 1)

    return ans


for j in range(h):
    for i in range(w):
        ans = max(ans, bfs(j, i))

print(ans)