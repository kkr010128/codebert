from itertools import permutations as p
from math import factorial as f
from math import sqrt as s

def func(x1, x2, y1, y2): return s((x2-x1) ** 2 + (y2-y1) ** 2)

N = int(input())
xy = list(list(map(int,input().split())) for _ in range(N))

total = 0

for l in p(range(1, N+1)):
  for i in range(N-1):
    total += func(xy[l[i]-1][0], xy[l[i+1]-1][0], xy[l[i]-1][1], xy[l[i+1]-1][1])

print(total / f(N))