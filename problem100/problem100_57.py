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

x = I()
if 400 <= x <= 599:
    print(8)
elif 600 <= x <= 799:
    print(7)
elif 800 <= x <= 999:
    print(6)
elif 1000 <= x <= 1199:
    print(5)
elif 1200 <= x <= 1399:
    print(4)
elif 1400 <= x <= 1599:
    print(3)
elif 1600 <= x <= 1799:
    print(2)
elif 1800 <= x <= 1999:
    print(1)