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

k = I()
s = input()
n = len(s)

fact = [1] * (n + k + 1)
for i in range(1, n+k+1):
    fact[i] = i * fact[i-1]
    fact[i] %= mod
ans = 0
for i in range(n, n + k + 1):
    ret = fact[i-1] * pow(fact[n-1], mod-2, mod) * pow(fact[i-n], mod-2, mod) % mod
    ret *= pow(25, i - n, mod)
    ret %= mod
    ret *= pow(26, k + n - i, mod)
    ret %= mod
    ans += ret
    ans %= mod
print(ans)