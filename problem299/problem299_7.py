import sys
import numpy as np
import numba
from numba import jit

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@jit
def main(n, a):
  ans = np.zeros(n)
  for i, j in enumerate(a):
    ans[j-1] = i+1
  for i in ans:
    print(int(i), end=' ')
n = int(readline())
a = np.array(readline().split(), np.int64)
main(n,a)