h, w, k = list(map(int, input().split()))

grid = [input() for _ in range(h)]
ans = [[0]*w for _ in range(h)]

cnt = 0

for j in range(h):
    for i in range(w):
        if grid[j][i] == "#":
            cnt += 1
            l = i
            r = i
            u = j
            d = j

            moving = True
            while moving and l > 0:
                moving = False
                if ans[j][l-1] == 0 and grid[j][l-1] == ".":
                    moving = True
                    l -= 1

            moving = True
            while moving and r < w-1:
                moving = False
                if ans[j][r+1] == 0 and grid[j][r+1] == ".":
                    moving = True
                    r += 1

            moving = True
            while moving and u > 0:
                moving = False
                canMove = True

                for x in range(l, r+1):
                    if not (ans[u-1][x] == 0 and grid[u-1][x] == "."):
                        canMove = False
                        break

                if canMove:
                    moving = True
                    u -= 1

            moving = True
            while moving and d < h-1:
                moving = False
                canMove = True

                for x in range(l, r+1):
                    if not (ans[d+1][x] == 0 and grid[d+1][x] == "."):
                        canMove = False
                        break

                if canMove:
                    moving = True
                    d += 1

            for y in range(u, d+1):
                for x in range(l, r+1):
                    ans[y][x] = cnt

for row in ans:
    print(" ".join(map(str, row)))