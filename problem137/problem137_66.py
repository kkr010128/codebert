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
import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    a = []
    b = []
    for _ in range(n):
        ai, bi = ns()
        a.append(ai)
        b.append(bi)

    a.sort()
    b.sort()

    if n % 2:
        ans = b[n // 2] - a[n // 2] + 1
    else:
        ans = b[n // 2] + b[n // 2 - 1] - (a[n // 2] + a[n // 2 - 1]) + 1
    print(ans)


if __name__ == '__main__':
    main()
