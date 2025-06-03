import sys
from heapq import heapify, heappush, heappop

read = sys.stdin.read
readline = sys.stdin.readline

H, W = map(int, readline().split())
s = tuple(map(str, read().split()))
INF = 10 ** 10
grid = [[INF] * W for _ in range(H)]
if s[0][0] == '#':
    start = (1, (0, 0))
else:
    start = (0, (0, 0))
heap = [start]
heapify(heap)
while heap:
    d, (x, y) = heappop(heap)
    if grid[x][y] != INF:
        continue
    grid[x][y] = d
    for i, j in ((0, 1), (1, 0)):
        new_x = x + i
        new_y = y + j
        if new_x == H or new_y == W:
            continue
        if grid[new_x][new_y] <= d:
            continue
        if s[x][y] == '.' and s[new_x][new_y] == '#':
            heappush(heap, (d + 1, (new_x, new_y)))
        else:
            heappush(heap, (d, (new_x, new_y)))

print(grid[-1][-1])
