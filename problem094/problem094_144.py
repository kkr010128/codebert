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

r, c, k = LI()
maze = [[0] * c for _ in range(r)]
for _ in range(k):
    R, C, V = LI()
    maze[R-1][C-1] = V

dp1 = [[0] * (c+1) for _ in range(r+1)]
dp2 = [[0] * (c+1) for _ in range(r+1)]
dp3 = [[0] * (c+1) for _ in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        dp1[i][j] = max(dp1[i][j-1], dp1[i-1][j] + maze[i-1][j-1], maze[i-1][j-1], dp2[i-1][j] + maze[i-1][j-1], dp3[i-1][j] + maze[i-1][j-1])
        dp2[i][j] = max(dp2[i][j-1], dp2[i-1][j], dp1[i][j-1] + maze[i-1][j-1])
        dp3[i][j] = max(dp3[i][j-1], dp3[i-1][j], dp2[i][j-1] + maze[i-1][j-1])
ans = max(dp1[-1][-1], dp2[-1][-1], dp3[-1][-1])
print(ans)