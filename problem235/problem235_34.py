import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
from itertools import accumulate
from itertools import permutations
from itertools import combinations
from collections import defaultdict
from collections import Counter
import fractions
import math
from collections import deque
from bisect import bisect_left
from bisect import bisect_right
from bisect import insort_left
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import heapq
from copy import deepcopy
from decimal import Decimal
alf = list("abcdefghijklmnopqrstuvwxyz")
ALF = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
MOD = 10**9+7
N = int(input())
A = list(map(int,input().split()))
L = A[0]
for i in range(1,N):
    g = math.gcd(L,A[i])
    L = L*A[i]//g
ans = 0
L %= MOD
for i in range(N):
    ans += (L*pow(A[i],MOD-2,MOD))
    ans %= MOD
print(ans)