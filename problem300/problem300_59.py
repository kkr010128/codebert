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
a,b=mi()
while a!=0:
  c=a
  a=b%a
  b=c
ans=1
for i in range(2,int(math.sqrt(b)+2)):
  if b%i==0:
    ans+=1
    while b%i==0:
      b=int(b/i)
if b!=1:
    ans+=1
print(ans)