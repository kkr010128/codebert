import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===

def main():
    worst_score = 10 ** 12

    n, k = ns()
    a = na()
    f = na()
    a.sort()
    f.sort(reverse=True)
    score = [ai * fi for ai, fi in zip(a, f)]

    l = -1
    r = worst_score + 1

    while r - l > 1:
        middle = (l + r) // 2
        tmp_k = k
        for i in range(n):
            tmp = math.ceil((score[i] - middle) / f[i])
            tmp_k -= max(0, tmp)

            if tmp_k < 0:
                break

        if tmp_k >= 0:
            r = middle
        else:
            l = middle
    print(r)

if __name__ == '__main__':
    main()
