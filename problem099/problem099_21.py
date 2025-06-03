import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
INF = 10**9

def ok(l):
    cnt = 0
    for L in a:
        cnt += L//l
        if L%l != 0:
            cnt+=1
        cnt-=1
    return cnt <= k

if __name__ == "__main__":
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    left = 0
    right = max(a)
    #最大値の最小値は二分探索
    while right - left > 1:
        mid = (right+left)//2
        if ok(mid):
            right = mid
        else:
            left = mid
    print(right)