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
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

s=input()
lns=len(s)
lst=[0]*(lns+1)

start=[]
if s[0]=="<":
    start.append(0)
for i in range(lns-1):
    if s[i]==">" and s[i+1]=="<":
        start.append(i+1)
if s[lns-1]==">":
    start.append(lns)

for i in start:
    d=deque([[i,0],[i,1]])
    while d:
        now,lr=d.popleft()
        # print(now)
        if now-1>=0 and lr==0 and s[now-1]==">":
            lst[now-1]=max(lst[now-1],lst[now]+1)
            d.append([now-1,0])
        if now+1<=lns and lr==1 and s[now]=="<":
            lst[now+1]=max(lst[now+1],lst[now]+1)
            d.append([now+1,1])
    # print(lst)
# print(start)
# print(lst)
print(sum(lst))