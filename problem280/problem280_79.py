from itertools import permutations
import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

sum_roots = 0
for points in permutations(XY):
    for point_idx in range(1, N):
        before_x = points[point_idx-1][0]
        before_y = points[point_idx-1][1]
        x = points[point_idx][0]
        y = points[point_idx][1]
        sum_roots += math.sqrt((x-before_x) ** 2 + (y-before_y)**2)

print(sum_roots/math.factorial(N))
