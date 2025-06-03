from collections import deque
h, w = list(map(int, input().split()))
grid = [input() for _ in range(h)]

ans = [[10000]*w for _ in range(h)]
ans[0][0] = 0 if grid[0][0] == "." else 1

queue = deque([(0, 0)])

while len(queue) > 0:
    x, y = queue.popleft()

    for xo, yo in [(0, 1), (1, 0)]:
        xnext, ynext = x+xo, y+yo

        if xnext >= w or ynext >= h:
            continue

        if grid[y][x] == "." and grid[ynext][xnext] == "#":
            if ans[y][x] + 1 < ans[ynext][xnext]:
                ans[ynext][xnext] = ans[y][x] + 1
                queue.append((xnext, ynext))
        else:
            if ans[y][x] < ans[ynext][xnext]:
                ans[ynext][xnext] = ans[y][x]
                queue.append((xnext, ynext))

print(ans[h-1][w-1])