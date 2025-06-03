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
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    h,n = map(int,ipt().split())
    atks = [tuple(map(int,ipt().split())) for i in range(n)]
    dam = [10**18]*(h+1)
    dam[0] = 0
    for i in range(1,h+1):
        for aj,bj in atks:
            if aj > i:
                if dam[i] > bj:
                    dam[i] = bj
            elif dam[i] > dam[i-aj]+bj:
                dam[i] = dam[i-aj]+bj

    print(dam[h])

    return None

if __name__ == '__main__':
    main()
