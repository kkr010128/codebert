import numpy as np
from copy import deepcopy
from heapq import heappop, heappush
from bisect import bisect_left, bisect
from collections import Counter, defaultdict, deque
from itertools import product, permutations, combinations

H, W, K = map(int, input().split())
c = np.zeros((W, H))

for h in range(H):
    s = list(input())
    for w in range(W):
        if s[w] == ".":
            c[w, h] = 0
        else:
            c[w, h] = 1

n = 0

for wt in product([1, 0], repeat=W):
    for ht in product([1, 0], repeat=H):
        d = deepcopy(c)
        for i in range(W):
            if wt[i] == 1:
                d[i, :] = 0
        for i in range(H):
            if ht[i] == 1:
                d[:, i] = 0
        if np.count_nonzero(d) == K:
            n += 1
print(n)
exit()
