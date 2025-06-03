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

N = int(input())
A = list(map(int, input().split()))

if N == 0:
    if A[0] == 1:
        print(1)
        exit()
    else:
        print(-1)
        exit()
if N != 0 and A[0] > 0:
    print(-1)
    exit()

rcA = [0] * (N)
rcA[-1] = A[-1]
for i in range(1, N):
    rcA[-i - 1] = rcA[-i] + A[-i - 1]
# print(rcA)

cnt = 1
node = 1
for a, rca in zip(A, rcA):
    min_node = node - a
    max_node = 2 * (node - a)
    if rca < min_node or min_node < 0:
        print(-1)
        exit()
    node = min(max_node, rca)
    # print(node)
    cnt += node
if node != A[-1]:
    print(-1)
    exit()
print(cnt)