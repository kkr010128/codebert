import sys
import itertools
sys.setrecursionlimit(10000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy

if __name__ == "__main__":
    a,b,c,d = map(int,input().split())
    e = a*c
    f = a*d
    g = b*c
    h = b*d
    ans = max(e,f)
    ans = max(ans,g)
    ans = max(ans,h)
    print(ans)