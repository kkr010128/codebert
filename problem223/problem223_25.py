# coding=UTF-8
from collections import deque
from operator import itemgetter
from bisect import bisect_left, bisect
import itertools
import sys
import math
import numpy as np
import time
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def ev(n):
    return 0.5*(n+1)


def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    p_ev = list(map(ev, p))

    s = np.cumsum(p_ev)
    s = np.insert(s, 0, 0)

    ans = []

    for i in range(n - k+1):
        ans.append(s[i + k] - s[i])

    print(max(ans))


if __name__ == '__main__':
    main()
