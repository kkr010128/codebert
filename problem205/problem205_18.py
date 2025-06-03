import sys

# import bisect
# from collections import Counter, deque, defaultdict
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter

# import math

# from numba import jit

# from scipy import
# import numpy as np
# import networkx as nx

# import matplotlib.pyplot as plt

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, p = list(map(int, readline().split()))
    s = input()

    ans = 0

    if p == 2 or p == 5:
        for i in range(n):
            if int(s[i]) % p == 0:
                ans += (i + 1)
    else:
        c = [0] * p
        prev = 0
        c[0] = 1
        for i in range(n):
            num = int(s[n - i - 1])
            m = (num * pow(10, i, p) + prev) % p
            c[m] += 1
            prev = m

        for i in range(p):
            cnt = c[i]
            ans += cnt * (cnt - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
