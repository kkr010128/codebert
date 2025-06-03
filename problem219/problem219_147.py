'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7
# mod = 998244353
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"
INF = 1<<32-1
# INF = 10**18

def main():
    ans = 0
    n = input()
    dp = [0,1] #0,1多く入れる
    for i in n:
        ni = int(i)
        pdp = dp*1
        dp[0] = min(pdp[0]+ni,pdp[1]+(10-ni))
        dp[1] = min(pdp[0]+ni+1,pdp[1]+(10-ni-1))
    print(dp[0])


    return None

if __name__ == '__main__':
    main()
