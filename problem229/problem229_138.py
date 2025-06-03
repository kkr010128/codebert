# coding: utf-8
import sys
# from operator import itemgetter
sysread = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10 ** 7)
from heapq import heappop, heappush
#from collections import defaultdict
# import math
# from itertools import product, accumulate, combinations, product
# import bisect# lower_bound etc
#import numpy as np
# from copy import deepcopy
#from collections import deque
#import numba

def run():
    H, N = map(int, sysread().split())
    AB = list(map(int, read().split()))
    A = AB[::2]
    B = AB[1::2]
    Amax = max(A)

    INF = float('inf')
    dp = [[INF] * (H+Amax+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(H+Amax+1):
            tmp = j - A[i]
            if tmp >= 0:
                dp[i+1][j] = min([dp[i][j], dp[i+1][tmp] + B[i]])
            elif j == H and tmp < 0:
                dp[i + 1][H] = min(dp[i][H], dp[i + 1][0] + B[i])
            else:
                dp[i+1][j] = dp[i][j]
    ret = min(dp[N][H:])
    print(ret)



if __name__ == "__main__":
    run()