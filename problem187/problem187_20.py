import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy
import bisect

if __name__ == "__main__":
    n,x,y = map(int,input().split())
    x-=1
    y-=1
    ans = [0]*(n)
    for i in range(n):
        for j in range(i+1,n):
            d = min(abs(i-j),abs(x-i) + abs(y-j) + 1)
            ans[d] += 1
    for i in range(1,n):
        print(ans[i])