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
    n, t = ns()
    d = [na() for _ in range(n)]
    d.sort()

    dp = [-1 for _ in range(t + 3000 + 1)]
    dp[0] = 0

    for a, b in d:
        for i in range(t - 1, -1, -1):
            if dp[i] >= 0:
                dp[i + a] = max(dp[i + a], dp[i] + b)

    print(max(dp))


if __name__ == '__main__':
    main()
