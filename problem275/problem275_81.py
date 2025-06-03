#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**8)
inf = float('inf')
ans = count = 0

A=list(map(int,input().split()))
for ai in A:
    if ai==1:
        ans+=300000
    elif ai==2:
        ans+=200000
    elif ai==3:
         ans+=100000
if A[0]==1 and A[1]==1:
    ans+=400000
print(ans)