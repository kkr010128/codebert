from collections import *
from heapq import *
import sys
input=lambda :sys.stdin.readline().rstrip()


N=int(input())
A=list(map(int,input().split()))
mod=10**9+7
count=1
lst=[0,0,0]
for a in A:
    data=[i for i in range(3) if lst[i] == a]
    if not data:
        count=0
        break
    count*=len(data)
    count%=mod
    i=data[0]
    lst[i]+=1
print(count)
