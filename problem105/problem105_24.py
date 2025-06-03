# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


N = z()
A = zz()
ans = 0
for i, a in enumerate(A):
    if(((i+1) % 2 == 1) and(a % 2 == 1)):
        ans += 1
print(ans)
