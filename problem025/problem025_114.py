import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
import bisect
import functools

@functools.lru_cache(None)
def dfs(i,sum_v,val):
    if i == n:
        return sum_v == val
    if dfs(i+1,sum_v,val):
        return True
    if dfs(i+1,sum_v + A[i],val):
        return True
    return False
n = int(input())
A = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

for i in range(q):
    if dfs(0,0,m[i]):
        print("yes")
    else:
        print("no")


