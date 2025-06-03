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
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        ans+=a[i]*a[j]
print(ans)