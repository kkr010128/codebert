from itertools import combinations

import math
N = int(input())

x = []
y = []

for i in range(N):
    _x, _y = map(int, input().split())
    x.append(_x)
    y.append(_y)
    
s = 0
for c in combinations(zip(x, y), 2):
    s += math.sqrt((c[0][0] - c[1][0]) ** 2 + (c[0][1] - c[1][1]) ** 2)

print(s * 2 / N)