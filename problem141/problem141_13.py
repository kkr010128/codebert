#!/usr/bin/env python3
 
import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
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
a = LI()
L = [1]
if a[-1] > 2**n:
    print(-1)
    quit()
if n == 0:
    if a[0] == 0:
        print(-1)
        quit()
L2 = [a[-1]]
for i in range(n)[::-1]:
    L2.append(min(L2[-1] + a[i], 2**i))
L2 = L2[::-1]
ans = 0
for i in range(n+1):
    if i == 0:
        tmp = 1
    else:
        tmp = (L[-1] - a[i-1]) * 2
    if tmp <= 0:
        print(-1)
        quit()
    ans += min(tmp, L2[i])
    L.append(tmp)
if L[-1] - a[-1] < 0:
    print(-1)
    quit()
print(ans)
