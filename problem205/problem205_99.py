import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

N, P = map(int, input().split())
S = list(map(int, input()))

if P == 2:
    print(sum(i + 1 for i in range(N) if S[i] % 2 == 0))
elif P == 5:
    print(sum(i + 1 for i in range(N) if S[i] % 5 == 0))
else:
    x = [None] * (N + 1)
    x[N] = 0
    tmp = 1
    for i in reversed(range(N)):
        x[i] = (x[i + 1] + S[i] * tmp) % P
        tmp = tmp * 10 % P
    print(sum(i * (i - 1) // 2 for i in Counter(x).values()))

