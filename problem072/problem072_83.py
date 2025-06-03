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
    n = int(ipt())
    cnt = 0
    for i in range(n):
        a,b = map(int,ipt().split())
        if a == b:
            if cnt == 2:
                print("Yes")
                exit()
            else:
                cnt += 1
        else:
            cnt = 0
    print("No")

    return None

if __name__ == '__main__':
    main()
