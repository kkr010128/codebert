import sys
import re
import math
import collections
import decimal
import bisect

# import copy
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
    a, b, c = ns()
    tmp = decimal.Decimal(a).sqrt() + decimal.Decimal(b).sqrt() - decimal.Decimal(c).sqrt()
    print("Yes" if tmp < 0 else "No")


if __name__ == '__main__':
    main()
