s = int(input())
mod = 10**9+7
import numpy as np

if s == 1 or s == 2:
  print(0)
elif s == 3:
  print(1)
else:
  array = np.zeros(s+1)
  array[0] = 1
  for i in range(3, s+1):
    array[i] = np.sum(array[:i-2]) % mod
  print(int(array[s]))
