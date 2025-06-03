import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *

sys.setrecursionlimit(100000000)


def input(): return sys.stdin.readline().rstrip()


N, K, C = map(int, input().split())
S = input()

L = [None] * K
R = [None] * K

i = 0
for j in range(N):
    if S[j] == 'o' and i < K and (i == 0 or j - L[i - 1] > C):
        L[i] = j
        i += 1

i = K - 1
for j in reversed(range(N)):
    if S[j] == 'o' and i >= 0 and (i == K - 1 or R[i + 1] - j > C):
        R[i] = j
        i -= 1

for l, r in zip(L, R):
    if l == r:
        print(l + 1)
