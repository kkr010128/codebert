from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import product, combinations,permutations
from copy import deepcopy
import sys
from math import sqrt
sys.setrecursionlimit(4100000)



if __name__ == '__main__':
    N = int(input())

    max_N = int(sqrt(N))+2
    ans = 10e13
    for a in range(1, max_N):
        if N%a==0:
            b = N//a
            ans = min(ans, a+b-2)
    print(ans)