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

s=input()
n=len(s)
ans=0
for i in range(n//2):
    if s[i]!=s[-1-i]:
        ans+=1
print(ans)