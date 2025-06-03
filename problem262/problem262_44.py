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
# INF =  float("inf")
INF = 10**18
import bisect
import statistics
mod = 10**9+7
# mod = 998244353

def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

N = int(input())

x = [[] for i in range(N)]
for i in range(N):
    A = int(input())
    for j in range(A):
        p, q = map(int, input().split())
        x[i].append([p-1, q])

ans = 0
for i in range(0,2**N):
    flag = 1
    for j in range(N):
        if ((i >> j) & 1):
            for xx in x[j]:
                if xx[1] == 1:
                    if not ((i >> xx[0]) & 1):
                        flag = 0
                        break
                else:
                    if ((i >> xx[0]) & 1):
                        flag = 0
                        break

        if flag == 0:
            break

    if flag == 0:
        continue
    else:
        ans = max(ans, popcount(i))

print(ans)




