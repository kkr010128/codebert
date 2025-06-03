#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left, bisect_right #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep='\n')

N = int(input())
A = list(map(int, input().split()))
A.sort()
C = Counter(A)
S = set(A)

maxA = A[-1]
chk = [0] * (maxA+1)
for s in S:
    for i in range(s, maxA+1, s):
        chk[i] += 1

res = [s for s in S if chk[s] == 1 and C[s] == 1]
# print(res)
print(len(res))