#!/usr/bin/env python3
#ABC146 E

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

"""
S := aの累積和
(Sj - Si) % k = j - i
ある整数mに対して
Sj - Si = m*k + j - i
Sj - j = m*k + Si - i
(Sj - j) - (Si - i) Ξ 0 (mod k)
(Sj - j) Ξ (Si - i) (mod k)
"""
n,k = LI()
a = LI()
s = [0] + list(accumulate(a))
ans = 0
d = defaultdict(int)
for j in range(n+1):
    t = (s[j] - j) % k
    if j >= k:
        x = (s[j-k] - (j-k)) % k
        d[x] -= 1
    ans += d[t]
    d[t] += 1
print(ans)
    
