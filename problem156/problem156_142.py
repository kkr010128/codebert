import sys
from collections import deque, defaultdict, Counter
from itertools import accumulate, product, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from math import ceil, floor, sqrt, gcd, inf
from copy import deepcopy
import numpy as np
import scipy as sp

INF = inf
MOD = 1000000007

x = int(input())

tmp = [i ** 5 for i in range(ceil(x ** 0.25) + 1)]
res = 0

for a in range(len(tmp) - 1):
    for b in range(a + 1, len(tmp)):
        if tmp[a] - tmp[b] == x:
            res = f"{a} {b}"
            break
        elif tmp[a] + tmp[b] == x:
            res = f"{a} {-b}"
            break
        elif -tmp[a] + tmp[b] == x:
            res = f"{-a} {-b}"
            break
        elif -tmp[a] - tmp[b] == x:
            res = f"{-a} {b}"
            break

print(res)
