def dist(x0, y0, x1, y1):
    from math import sqrt
    return sqrt((x1-x0)**2 + (y1-y0)**2)

from itertools import permutations

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)] #; print(points)

dsum = 0
for i, j in permutations(points, 2):
    dsum += dist(*i, *j)
print(dsum/N)