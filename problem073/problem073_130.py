import numpy as np

n = int(input())
count = np.zeros(n, dtype=np.int)
for d in range(1, n):
  count[d::d] += 1
print(count.sum())