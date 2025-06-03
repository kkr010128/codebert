import math
import collections
import fractions
import itertools
import functools
import operator
import numpy as np

def solve():
    h, w = map(int, input().split())
    maze = [input() for _ in range(h)]
    ans = 0
    can_move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for x in range(h):
        for y in range(w):
            if maze[x][y] == "#":
                continue
            dist = [[0]*w for _ in range(h)]
            stack = collections.deque()
            stack.append([x,y])
            while stack:
                h2, w2 = stack.popleft()
                for i, j in can_move:
                    newh, neww = h2+i, w2+j
                    if newh < 0 or neww < 0 or newh >= h or neww >= w:
                        continue
                    elif maze[newh][neww] != "#" and dist[newh][neww] == 0:
                        dist[newh][neww] = dist[h2][w2]+1
                        stack.append([newh, neww])
            dist[x][y] = 0
            ans = max(ans, np.max(dist))
    print(ans)
    return 0

if __name__ == "__main__":
    solve()