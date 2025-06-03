#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,m=map(int,input().split())
A=sorted(map(int,input().split()))
B=[0]+A[:]
for i in range(n):
    B[i+1]+=B[i]

def solve_binary(mid):
    tmp=0
    for i,ai in enumerate(A):
        tmp+=n-bisect.bisect_left(A,mid-ai)
    return tmp>=m

def binary_search(n):
    ok=0
    ng=n
    while abs(ok-ng)>1:
        mid=(ok+ng)//2
        if solve_binary(mid):
            ok=mid
        else:
            ng=mid
    return ok

binresult=binary_search(2*10**5+1)
for i ,ai in enumerate(A):
    ans+=ai*(n-bisect.bisect_left(A,binresult-ai))+B[n]-B[bisect.bisect_left(A,binresult-ai)]
    count+=n-bisect.bisect_left(A,binresult-ai)
    # print(ans,count)
ans-=binresult*(count-m)
print(ans)
# print(binresult)