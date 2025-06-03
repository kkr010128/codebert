import numpy as np
from numba import njit

@njit
def update(a):
  n = len(a)
  b = np.zeros_like(a)
  for i,x in enumerate(a):
    l = max(0, i-x)
    r = min(n-1, i+x)
    b[l] += 1
    if r+1 < n:
      b[r+1] -= 1
  b = np.cumsum(b)
  return b

n,k = map(int, input().split())
a = np.array(list(map(int, input().split())))

for _ in range(k):
  a = update(a)
  if np.all(a==n):
    break
    
print(' '.join(map(str, a)))