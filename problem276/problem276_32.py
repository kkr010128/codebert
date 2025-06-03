import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(500000)
mod=10007
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
a=list(map(int,input().split()))
lst=ruiseki(a)
asum=sum(a)
# print(asum)
# print(lst)
cnt=bisect.bisect_left(lst,asum/2)
# print(cnt)
if asum//2==lst[cnt]:
    print(0)
else:
    if asum%2==0:
        print(2*min(asum//2-lst[cnt-1],lst[cnt]-asum//2))
    else:
        print(min((asum//2-lst[cnt-1])*2+1,(lst[cnt]-asum//2)*2-1))