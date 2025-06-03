# import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial, gcd
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10 ** 7)
enu = enumerate
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep="\n")

N = int(input())
L = [input() for _ in range(N)]

up = []
do = []
for li in L:
    l = li.count("(")
    r = li.count(")")
    ext_neg = 0
    ext_pos = 0
    tl, tr = 0, 0
    if 0 <= l - r:
        for op in li:
            if op == "(":
                tl += 1
            elif op == ")":
                tr += 1
            ext_neg = min(ext_neg, tl - tr)
            ext_pos = max(ext_pos, tl - tr)
        up.append((l - r, ext_neg, ext_pos))
    else:
        for op in li[::-1]:
            if op == ")":
                tl += 1
            elif op == "(":
                tr += 1
            ext_neg = min(ext_neg, tl - tr)
            ext_pos = max(ext_pos, tl - r)
        do.append((r - l, ext_neg, ext_pos))
up.sort(key=lambda tup: (-tup[1], -tup[0]))
do.sort(key=lambda tup: (-tup[1], -tup[0]))
# print(up)
# print(do)

curl = 0
for upi in up:
    dif, ext_neg, ext_pos = upi
    if curl + ext_neg < 0:
        print("No")
        exit()
    curl += dif
curr = 0
for doi in do:
    dif, ext_neg, ext_pos = doi
    if curr + ext_neg < 0:
        print("No")
        exit()
    curr += dif
if curl == curr:
    print("Yes")
else:
    print("No")
