import math
import itertools
from statistics import mean
n = int(input())
p = [list(map(int,input().split())) for i in range(n)]
ans = []
for v in itertools.permutations(p):
  length = 0
  for i in range(n-1):
    length += math.sqrt((v[i+1][0] - v[i][0])**2 + (v[i+1][1] - v[i][1])**2)
  ans.append(length)

print(mean(ans))