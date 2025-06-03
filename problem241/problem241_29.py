from collections import deque

def input_bordered_grid(h, w, wall):
    grid = [wall * (w + 2)]
    for _ in range(1, h+1):
        grid.append(wall + input() + wall)
    grid.append(wall * (w + 2))
    return grid

h, w = map(int, input().split())
grid = input_bordered_grid(h, w, '#')

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

longest = 0
for sy in range(1, h+1):
    for sx in range(1, w+1):
        if grid[sy][sx] == '#':
            continue
        dist = [[-1] * (w+2) for _ in range(h+2)]
        dist[sy][sx] = 0
        q = deque()
        q.append((sy, sx))
        while q:
            y, x = q.popleft()
            longest = max(longest, dist[y][x])
            for dy, dx in move:
                yy = y + dy
                xx = x + dx
                if dist[yy][xx] == -1 and grid[yy][xx] == '.':
                    q.append((yy, xx))
                    dist[yy][xx] = dist[y][x] + 1
print(longest)
