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

n,k=mp()
h=sorted(lmp())
if n<=k:
    print(0)
else:   
    print(sum(h[:n-k]))