N = int(input())
XY = []
points = []
for i in range(N):
	points.append(i)
	x, y = list(map(int, input().split()))
	XY.append((x, y))

import math
import itertools
count = math.factorial(N)
line = 0
for pp in itertools.permutations(points, N):
	i = 0
	while i < N - 1:
		i1, i2 = pp[i], pp[i + 1]
		t = ((XY[i1][0] - XY[i2][0]) ** 2 + (XY[i1][1] - XY[i2][1]) ** 2) ** 0.5 
		line += t
		i += 1
ans = line / count
print(ans)
