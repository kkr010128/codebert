'''
研究室PCでの解答
'''
import math
#import numpy as np
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
#setrecursionlimit(10**7)
mod = 10**9+7
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    n,k = map(int,ipt().split())
    a = [int(i) for i in ipt().split()]

    memo = deque()
    memo.append(0)
    d = defaultdict(int)
    ans = 0
    nv = 0
    d[0] += 1
    for i,ai in enumerate(a):
        nv += ai-1
        nv %= k
        memo.append(nv)
        if i >= k-1:
            pi = memo.popleft()
            d[pi] -= 1
        ans += d[nv]
        d[nv] += 1

    print(ans)

    return None

if __name__ == '__main__':
    main()
