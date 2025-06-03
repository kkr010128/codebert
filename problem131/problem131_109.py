from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce, lru_cache  # @lru_cache(None)
from fractions import gcd
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
# ----------------------------------------------------------- #

a, v = (int(x) for x in input().split())
b, w = (int(x) for x in input().split())
t = int(input())

if a == b:
    print("YES")
elif a < b:
    if a + t*v >= b + t*w:
        print("YES")
    else:
        print("NO")
else:
    if a - t*v <= b - t*w:
        print("YES")
    else:
        print("NO")