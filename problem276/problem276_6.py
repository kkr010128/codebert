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

n=int(input())
a=lmp()
x=0
y=sum(a)
ans=abs(x-y)
for i in range(n):
    x+=a[i]
    y-=a[i]
    ans=min(ans,abs(x-y))
print(ans)