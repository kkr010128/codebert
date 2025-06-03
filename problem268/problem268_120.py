# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
from heapq import heappop, heappush
from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product, accumulate, combinations, product
#import bisect
#import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50
EPS = 1e-8
mod = 10 ** 9 + 7

def mapline(t = int):
    return map(t, sysread().split())
def mapread(t = int):
    return map(t, read().split())

def run():
    N, *A = mapread()
    ans = 1
    current = [0,0,0]
    for a in A:
        transition = 0
        cache = None
        for i, c in enumerate(current):
            if c == a:
                transition += 1
                cache = i
        ans *= transition
        ans %= mod
        if cache == None:
            print(0)
            return
        current[cache] += 1
        #print(current)
    print(ans)

if __name__ == "__main__":
    run()
