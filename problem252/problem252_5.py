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

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
left=0
right=(10**5)*2+5
s=ruiseki(a)

ans=0
while 1:
    mid=(left+right)//2
    cnt=0
    for i in range(n):
        tmp=bisect.bisect_left(a,mid-a[i])
        cnt+=n-tmp
    
    if cnt<m:
        right=mid
    else:
        left=mid
    
    # print(left,right,mid)
    if right-left<=1:
        break
for i in range(n):
    tmp=bisect.bisect(a,left-a[i])
    cnt=n-tmp
    ans+=cnt*a[i]+s[n]-s[tmp]
    m-=cnt
ans+=m*left
print(ans)