import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7

n,k=map(int,input().split())
a=list(map(int,input().split()))
f=list(map(int,input().split()))
left,right=-1,10**12+1
a.sort()
f.sort()
# print(a)
while right-left>1:
    mid=(right+left)//2
    tmp=0
    for i in range(n):
        tmp+=max(0,a[i]-mid//f[-1-i])
    
    if tmp<=k:
        right=mid
    else:
        left=mid
print(right)