# 町a,b(a < b)の距離をあらかじめdictionaryで保存しておく
# そのうえで、全探索可能

import sys
readline = sys.stdin.readline

N = int(readline())
town = [None] * N
for i in range(N):
  town[i] = tuple(map(int,readline().split()))

from collections import defaultdict
dist = defaultdict(float)

for i in range(N - 1):
  for j in range(i + 1, N):
    ix,iy = town[i]
    jx,jy = town[j]
    dist[(i,j)] = ((ix - jx) ** 2 + (iy - jy) ** 2) ** 0.5
    
# 距離を求めたので、あとは全パターン検索
ans = 0
import itertools
for perm in itertools.permutations(range(N)):
  d = 0
  for i in range(1, len(perm)):
    a,b = perm[i - 1],perm[i]
    if a > b:
      a,b = b,a
    d += dist[(a, b)]
  ans += d
  
pat = 1
for i in range(2, N + 1):
  pat *= i
print(ans / pat)