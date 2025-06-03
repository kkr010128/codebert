# import numpy as np
import sys, math, heapq
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial, gcd
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep="\n")

D, T, S = map(int, input().split())

if D / S > T:
    print("No")
else:
    print("Yes")
