import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, M =map(int, readline().split())
a = np.array(readline().split(), np.int64)
b = np.array(readline().split(), np.int64)

ans = a.min() + b.min()

for i in range(M):
  w = list(map(int, input().split()))
  new = a[w[0]-1] + b[w[1]-1] - w[2]
  ans = min(ans, new)
print(ans)