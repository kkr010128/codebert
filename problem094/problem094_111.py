import io
import os
from collections import defaultdict

DEBUG = False
if not DEBUG:

    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    R, C, K = [int(x) for x in input().split()]
    grid = [[0 for c in range(C)] for r in range(R)]
    for r, c, v in ((int(x) for x in input().split()) for i in range(K)):
        grid[r - 1][c - 1] = v
else:
    import random

    random.seed(0)
    R, C = 3000, 3000
    # 2 * 10**5 / 90 * 10**5 full
    grid = [
        [int(random.randint(1, 90) <= 2) * random.randint(0, 10 ** 9) for c in range(C)]
        for r in range(R)
    ]
    print(sum(bool(grid[r][c]) for r in range(R) for c in range(C)))
    print("done gen")

    from timeit import default_timer as timer

    startTime = timer()


currRow = [[0 for i in range(3 + 1)] for c in range(C + 1)]
prevRow = [0 for c in range(C + 1)]
nextPrevRow = [0 for c in range(C + 1)]

inf = float("inf")
for r in range(R):
    for c in range(C):
        for numTakenThisRow in range(3 + 1):
            best = max(
                currRow[c - 1][numTakenThisRow],  # came from left
                prevRow[c],  # came from top, didn't take curr
                currRow[c - 1][numTakenThisRow - 1] + grid[r][c]
                if numTakenThisRow
                else 0,  # came from left, took curr
                prevRow[c] + grid[r][c]
                if numTakenThisRow == 1
                else 0,  # came from top, took curr
            )
            currRow[c][numTakenThisRow] = best
        nextPrevRow[c] = max(currRow[c][i] for i in range(3 + 1))
    prevRow, nextPrevRow = nextPrevRow, prevRow
print(prevRow[C - 1])

if DEBUG:
    print(timer() - startTime)
