# Begin Header {{{
from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
# }}} End Header
# _________コーディングはここから！！___________
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for x in combinations(l, 3):
    if x[0]!=x[1] and x[0]!=x[2] and x[1]!=x[2]:
        if x[0] + x[1] > x[2]:
            ans+=1
print(ans)