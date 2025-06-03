# Begin Header {{{
from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
# }}} End Header
# _________コーディングはここから！！___________
mod = 10**9+7
n = int(input())
ans=0
ans+=pow(10, n, mod)
ans-=pow(9, n, mod)*2
ans+=pow(8, n, mod)
print(ans%mod)
