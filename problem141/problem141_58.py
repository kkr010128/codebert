import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
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

n=I()
lis=LI()
nleaf=[0 for i in range(n+1)]
nleaf[0]=1-lis[0]
if nleaf[0]<0:
    print(-1)
    sys.exit()
for i in range(n):
    nleaf[i+1]=nleaf[i]*2-lis[i+1]
    if nleaf[i+1]<0:
        print(-1)
        sys.exit()
#print(lis)
#print(nleaf)
u=list(reversed(lis))
sup=[0 for i in range(n+1)]
for i in range(n):
    sup[i+1]=min(sup[i]+u[i],nleaf[n-i-1])
    #print(sup[i]+u[i],nleaf[n-i-1])
    #print(min(sup[i]+u[i],nleaf[n-i-1]))
#print(sup)
print(sum(lis)+sum(sup))
    
    
        
