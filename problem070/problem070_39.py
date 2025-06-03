# coding: utf-8
import sys

# from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
printout = sys.stdout.write
sprint = sys.stdout.flush
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
#import math
# from itertools import product, accumulate, combinations, product
#import bisect
# import numpy as np
# from copy import deepcopy
from collections import deque
# from decimal import Decimal
# from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 998244353


def intread():
    return int(sysread())
def mapline(t=int):
    return map(t, sysread().split())
def mapread(t=int):
    return map(t, read().split())

def dfs(c, to, seen, g = None):
    if g == None:g = set()
    g.add(c)
    seen.add(c)
    for n in to[c]:
        if not n in seen:
            dfs(n, to, seen, g)
    return g, seen


def run():
    N, M = mapline()
    to = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = mapline()
        to[a].append(b)
        to[b].append(a)

    seen = set()
    G = []
    for i in range(1, N+1):
        if not i in seen:
            g, seen = dfs(i, to, seen)
            #print(i, seen)
            G.append(g)
    #print(G)
    print(len(G) -1)



if __name__ == "__main__":
    run()
