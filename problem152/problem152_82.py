#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n = I()
s = [input() for _ in range(n)]
x = [] #(の方が多いもの
y = [] #)の方が多いもの
for i in range(n):
    cnt1 = 0
    cnt2 = 0
    for j in range(len(s[i])):
        if s[i][j] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 - cnt2 > 0:
        x.append([cnt2, cnt1, s[i]])
    else:
        y.append([cnt1, cnt2, s[i]])
x.sort() #)が少ない順
y.sort(reverse=True) #(が多い順
tmp = 0
que = deque()
for i, j, k in x:
    for l in k:
        if l == '(':
            tmp += 1
        else:
            if tmp > 0:
                tmp -= 1
            else:
                print('No')
                quit()
for i, j, k in y:
    for l in k:
        if l == '(':
            tmp += 1
        else:
            if tmp > 0:
                tmp -= 1
            else:
                print('No')
                quit()
if tmp != 0:
    print('No')
else:
    print('Yes')