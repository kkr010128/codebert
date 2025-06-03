import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n,t = map(int,ipt().split())
    dp = [[0,0] for i in range(t)]
    for _ in range(n):
        a,b = map(int,ipt().split())
        for i in range(t-1,a-1,-1):
            di = dp[i][1]
            dpi = dp[i-a][1]+b
            if di < dpi:
                dp[i][1] = dpi
        for i in dp:
            if i[1] < i[0]+b:
                i[1] = i[0]+b
        for i in range(t-1,a-1,-1):
            di = dp[i][0]
            dpi = dp[i-a][0]+b
            if di < dpi:
                dp[i][0] = dpi

    print(dp[t-1][1])

    return

if __name__ == '__main__':
    main()
