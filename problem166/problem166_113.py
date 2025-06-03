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
    s = input()

    cnt = [0 for _ in range(2019)]
    cnt[0] += 1
    dec = 1
    num = 0
    for i in reversed(s):
        num += int(i) * dec
        num %= 2019
        dec *= 10
        dec %= 2019
        cnt[num] += 1

    ans = 0
    for c in cnt:
        ans += c * (c - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
