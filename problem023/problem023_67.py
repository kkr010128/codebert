import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy


n = int(input())
d = set()
for i in range(n):
    command,s = input().split()
    if command == "insert":
        d.add(s)
    else:
        if s in d:
            print("yes")
        else:
            print("no")

