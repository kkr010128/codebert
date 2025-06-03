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

eps = 10 ** (-9)


def main():
    n = ni()
    a = na()

    seta = set(a)
    cnta = collections.Counter(a)
    lista = list(seta)
    lista.sort()

    table = [True for _ in range(10 ** 6 + 1)]
    ans = 0

    for ai in lista:
        if table[ai]:
            if cnta[ai] == 1:
                ans += 1
            for i in range(ai, 10 ** 6 + 1, ai):
                table[i] = False

    print(ans)


if __name__ == '__main__':
    main()
