import math
import sys
from collections import deque
import heapq
import copy
import itertools
from itertools import permutations
from itertools import combinations
import bisect
def mi() : return map(int,sys.stdin.readline().split())
def ii() : return int(sys.stdin.readline().rstrip())
def i() : return sys.stdin.readline().rstrip()
a=ii()
l=list(mi())
l=sorted(l)
ans=0
for i in range(a-2):
  for j in range(i+1,a-1):
    s=bisect.bisect_left(l,l[i]+l[j])
    ans+=s-j-1
print(ans)