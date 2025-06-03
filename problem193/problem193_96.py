import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
from math import *

sys.setrecursionlimit(100000000)
input = lambda: sys.stdin.readline().rstrip()

H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
mi = None

def _max(iterable):
    ma = 0
    for i in iterable:
        ma = max(ma, i)
    return ma

for i in range(2 ** (H - 1)):
    # div[j] is true if row j and row j + 1 is divided
    div = [(i & (1 << j)) > 0 for j in range(H - 1)]
    group = [0] * H
    for j in range(H - 1):
        group[j + 1] = group[j] + 1 if div[j] else group[j]
    count = Counter()
    ans = div.count(True)
    ok = True
    for j in range(W):
        tmp = Counter()
        for k in range(H):
            if S[k][j] == '1':
                tmp[group[k]] += 1
        if _max(tmp.values()) > K:
            ok = False
        elif _max((tmp + count).values()) <= K:
            count += tmp
        else:
            count = tmp
            ans += 1
    if ok and (mi is None or ans < mi):
        mi = ans

print(mi)
