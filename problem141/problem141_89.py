import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi
from copy import deepcopy

# If you use recursive call, uncomment this code
sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 1
    befc = 1 - A[0] 
    if A[0] > 1:
        return -1
    tmp = sum(A[1::])
    for i in range(1,N+1):
        curc = min(befc * 2, tmp)
        if curc < A[i]:
            return -1
        ans += curc
        befc = curc - A[i]
        tmp -= A[i]
    return ans

if __name__ == '__main__':
    print(main())
