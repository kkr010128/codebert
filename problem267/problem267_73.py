from collections import defaultdict
from itertools import groupby, accumulate, product, permutations, combinations
from bisect import *
def solve():
  ans = 0
  N = int(input())
  S = input()
  d = defaultdict(lambda: [])
  for i,s in enumerate(S):
    d[int(s)].append(i)
  for p in product(range(10),repeat=3):
    if not len(d[p[0]]):
      continue
    ind1 = d[p[0]][0]
    ind2 = bisect_right(d[p[1]],ind1)
    if ind2==len(d[p[1]]):
      continue
    ind2 = d[p[1]][ind2]
    ind3 = bisect_right(d[p[2]],ind2)
    if ind3==len(d[p[2]]):
      continue
    ans += 1
  return ans
print(solve())