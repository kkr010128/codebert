import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

M=10**6+10
n=int(input())
a=Counter(lmp()).most_common()
a=sorted(a, key=lambda x: x[0])
c=[0]*M
for j,x in a:
    if c[j]==0:
        k=2
        while j*k<M:
            c[j*k]=1
            k+=1
ans=0
for x,y in a:
    if c[x]==0 and y==1:
        ans+=1
print(ans)