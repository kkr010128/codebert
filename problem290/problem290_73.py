import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A = sorted(A)
F = sorted(F, reverse=True)

def check(x):
    s = 0
    for i in range(N):
        s += max(0, A[i] - x // F[i])
    return s <= K

l = -1
r = 10 ** 18
while r - l > 1:
    m = (r + l) // 2
    if check(m):
        r = m
    else:
        l = m
print(r)