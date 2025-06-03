import sys
import re
import math
import collections
import decimal
import bisect
import itertools

import copy

# import heapq
# from collections import deque
# import decimal

# sys.setrecursionlimit(100001)
INF = sys.maxsize
# MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    s = list(input())
    k = ni()

    if len(set(s))==1:
        print((len(s)*k)//2)
        exit(0)

    def changer(sss):
        ts = sss.copy()
        cnt = 0
        for i in range(1, len(ts)):
            if ts[i] == ts[i - 1]:
                ts[i] = "@"
                cnt += 1

        return cnt

    print(changer(s) + (k - 1) * (changer(s + s) - changer(s)))


if __name__ == '__main__':
    main()
