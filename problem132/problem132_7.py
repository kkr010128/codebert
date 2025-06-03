import sys

# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
import heapq
import decimal
# import statistics
import queue


sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, k = ns()
    a = na()

    for _ in range(k):
        imos = [0 for _ in range(n)]

        for i, ai in enumerate(a):
            imos[max(0, i - ai)] += 1
            if i + ai + 1 < n:
                imos[i + ai + 1] -= 1

        val = 0
        for i, im in enumerate(imos):
            val += im
            a[i] = min(val, n)

        if min(a) == n:
            break

    print(*a, sep=" ")


if __name__ == '__main__':
    main()
