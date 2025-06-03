import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(str, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
#import numpy as np
from decimal import *
 
K = INT()


n = [-1]*11
cnt = 0

def DFS(n):
    global cnt
    for i in range(1, 11):
        if n[-i] == 9:
            continue
        elif n[-i-1] != -1 and n[-i] == n[-i-1]+1:
            continue
        else:
            if n[-i] == -1:
                n[-i] = 1
            else:
                n[-i] += 1

            for j in range(i-1, 0, -1):
                n[-j] = max(0, n[-j-1] - 1)
            break
    cnt += 1
    if cnt == K:
        print(*n[bisect(n, -1):], sep = "")
        exit()
    DFS(n)


DFS(n)
