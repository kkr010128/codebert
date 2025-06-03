import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product

def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,k=map(int,input().split())
a=list(map(int,input().split()))
# amari=[a[i]%k for i in range(n)]
rui=ruiseki(a)
# print(a)
# print(amari)
# print(rui)
dic=defaultdict(int)
ans=0
for i in range(n+1):
    if i>=k:
        dic[(rui[i-k]-(i-k))%k]-=1
    ans+=dic[(rui[i]-i)%k]
    dic[(rui[i]-i)%k]+=1
    # print(dic)
print(ans)