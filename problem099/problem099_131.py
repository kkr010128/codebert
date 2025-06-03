from sys import stdin
import numpy as np

n, k = map(int, stdin.buffer.readline().split())
a = np.fromstring(stdin.buffer.read(), dtype=np.int, sep=' ')

ng = 0
ok = 10 ** 9 + 1
while ok - ng > 1:
    mid = (ok + ng) >> 1
    if np.sum(np.ceil(a / mid) - 1) <= k:
        ok = mid
    else:
        ng = mid
print(ok)
