import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,m=map(int,input().split())
half=n//2
lst=[]
if n%2==1:
    for i in range(m):
        lst.append([half-i,half+i+1])
else:
    for i in range(m):
        if i%2==0:
            lst.append([half-i//2,half+i//2+1])
        else:
            lst.append([1+i//2,n-1-i//2])

for i in range(m):
    print(*lst[i])

# dic=defaultdict(int)
# for i in range(m):
#     tmp=lst[i]
#     dic[tmp[1]-tmp[0]]+=1
#     dic[n-tmp[1]+tmp[0]]+=1
# print(dic)
