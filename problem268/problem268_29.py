import sys

# import re
# import math
# import collections
# import decimal
# import bisect
# import itertools
# import fractions
# import functools
# import copy
# import heapq
# import decimal
# import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    n = ni()
    a = na()

    d = [0, 0, 0]

    ans = 1
    for ai in a:
        ans *= d.count(ai)
        ans %= MOD
        for i in range(3):
            if d[i] == ai:
                d[i] += 1
                break

    print(ans)


if __name__ == '__main__':
    main()
