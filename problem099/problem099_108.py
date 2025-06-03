import sys
import  math
import fractions
from collections import defaultdict
import heapq
from bisect import bisect_left,bisect

stdin = sys.stdin
     
ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

N,K=nm()
A=nl()
l=0
r=10**9
mid=0

if(K==0):
    print(max(A))
    sys.exit(0)

while(l+1<r):
    mid=(l+r)//2
    tmp=0
    for i in range(len(A)):
        tmp+=((A[i]-1)//mid)
    if(tmp<=K):
        r=mid
    else:
        l=mid

print(r)