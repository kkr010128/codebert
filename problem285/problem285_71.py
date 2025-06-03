# coding: utf-8
# hello worldと表示する
#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

s=SI()
if s[0]!="<":
    s="<"+s
if s[-1]!=">":
    s=s+">"
#print(s)
state="<"
strs=[]
count=0
for i in range(len(s)):
    if state=="<":
        if s[i]=="<":
            count+=1
        else:
            strs.append(count)
            count=1
            state=">"
    else:
        if s[i]==">":
            count+=1
        else:
            strs.append(count)
            count=1
            state="<"
strs.append(count)
#print(strs)
ans=0
for i in range(len(strs)//2):
    u=min(strs[2*i],strs[2*i+1])
    v=max(strs[2*i],strs[2*i+1])
    ans+=(u-1)*u//2+v*(v+1)//2
print(ans)