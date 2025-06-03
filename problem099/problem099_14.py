ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
n,k = ma()
A = list(ma())
A.sort(reverse=True)
if k==0:
    print(A[0])
    exit()

def isok(x):
    cnt=0
    for a in A:
        cnt+= (a-1)//x
    #print(cnt,x)
    return cnt>k
def bisect():
    ok = 0
    ng = 10**9+1
    x = (ok+ng)//2
    while ng-ok>1:
        if isok(x):
            ok = x
        else:
            ng=x
        x = (ok+ng)//2
    return ng
print(bisect())
