import math
from itertools import accumulate
n, k = map(int, input().split())
As = list(map(int, input().split()))
for i in range(min(41, k)):
  _As = [0]*(n+1)
  for j in range(n):
    l = max(0, j - As[j])
    r = min(n - 1, j + As[j])
    _As[l] += 1
    _As[r+1] -= 1
  As = list(accumulate(_As))[:-1]
print(' '.join([str(A) for A in As]))