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
    x,y = map(int,ipt().split())
    mas = [x+y,x-y,-x-y,y-x]
    ma = 0
    for _ in range(n-1):
        x,y = map(int,ipt().split())
        cpr = [-y-x,y-x,x+y,x-y]
        for i in range(4):
            if mas[i]+cpr[i] > ma:
                ma = mas[i]+cpr[i]
        for i in range(4):
            if mas[i] < cpr[i-2]:
                mas[i] = cpr[i-2]

    print(ma)
    return None

if __name__ == '__main__':
    main()
