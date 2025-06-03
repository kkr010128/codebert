from sys import stdin
from collections import defaultdict
N = int(stdin.readline().rstrip())
d = defaultdict(int)

for x in range(1,101):
  for y in range(1,101):
    for z in range(1,101):
      v = x**2 + y**2 + z**2 + x*y + y*z + z*x
      d[v] += 1

for i in range(1,N+1):
    print(d[i])