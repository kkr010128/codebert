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

def count(s):
    a = 0
    aa = 0
    b = 0
    bb = 0
    for i in range(len(s)):
        if s[i] == ")":
            if aa == 0:
                a = a + 1
            else:
                aa = aa - 1
        if s[i] == "(":
            aa = aa + 1
        if s[len(s)-1-i] == "(":
            if bb == 0:
                b = b + 1
            else:
                bb = bb - 1
        if s[len(s)-1-i] == ")":
            bb = bb + 1
    return [a, b]

N = int(input())

c = []
d = []
for i in range(N):
    s = input()
    e = count(s)
    if e[1] - e[0] >= 0: c.append(e)
    if e[0] - e[1] > 0: d.append(e)

c.sort(key=lambda x: x[0])
d.sort(key=lambda x: x[1], reverse=True)

c = c + d
# print(c)

f = 0
for cc in c:
    f = f - cc[0]
    if f < 0:
        print("No")
        sys.exit()
    f = f + cc[1]

if f == 0:
    print("Yes")
else:
    print("No")


