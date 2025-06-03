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

    dp = [defaultdict(lambda:0) for _ in range(N+1)]
    dp[0][(0,0,0)] = 1
    for i in range(N):
        a = A[i]
        k = i + 1
        for key in dp[k-1].keys():
            for ii, v in enumerate(key):
                if v == a:
                    tmp = list(key)
                    tmp[ii] += 1
                    dp[k][tuple(tmp)] += dp[k-1][key] % mod
    ans = 0
    for key in dp[N].keys():
        ans = (ans + dp[N][key]) % mod
    #print(dp)
    print(ans)


if __name__ == "__main__":
    run()
