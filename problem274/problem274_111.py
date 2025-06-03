from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter,defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
INF =  float("inf")
import bisect

N, M = list(map(int, input().split()))
S = input()

m = N
record = []
while True:
    for i in range(M,-1,-1):
        if i == 0:
            print(-1)
            sys.exit()
        if m-i < 0: continue
        if S[m-i] == "0":
            m = m - i
            record.append(str(i))
            if m == 0:
                print(" ".join(reversed(record)))
                sys.exit()
            break


