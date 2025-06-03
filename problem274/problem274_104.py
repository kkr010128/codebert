#!/usr/bin/env python3
#ABC146 F

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000)
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

n,m = LI()
s = input()

i = 0
cnt = 0
M = 0
while i < n+1:
    if s[i] == '1':
        cnt += 1
        M = max(M,cnt)
    else:
        cnt = 0
    i += 1
if M >= m:
    print(-1)
    quit()

lst = []
now = n
while now > 0:
    if now - m <= 0:
        lst.append(now)
        now -= m 
    else:
        for j in range(1,m+1)[::-1]:
            if s[now-j] == '0':
                lst.append(j)
                now -= j
                break
print(*lst[::-1])