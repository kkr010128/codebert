# input = sys.stdin.readline
from bisect import *
from collections import *
from heapq import *
# import functools
# import itertools
# import math
N,K=map(int,input().split())
A=list(map(int,input().split()))
F=list(map(int,input().split()))
A.sort()
F.sort(reverse=True)
def main(x):
    _K=K
    for i in range(N):
        a=A[i]-x//F[i]
        if a>0:
            _K-=a
            if _K<0:
                return(0)
    return(1)


end=10**12
if main(0):
    print(0)
    exit()
else:
    st=0

while end-st>1:
    now=(end+st)//2
    if main(now):
        end=now
    else:
        st=now

if main(st):
    print(st)
else:
    print(end)
