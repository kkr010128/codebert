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
# import heapq
import decimal
# import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, m = ns()
    c = na()

    dp = [INF for _ in range(n + 1)]
    dp[0] = 0

    for ci in c:
        for i in range(n + 1 - ci):
            dp[i + ci] = min(dp[i + ci], dp[i] + 1)

    print(dp[n])


if __name__ == '__main__':
    main()

