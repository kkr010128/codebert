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

def main():
    x = int(ipt())
    if x < 600:
        print(8)
    elif x < 800:
        print(7)
    elif x < 1000:
        print(6)
    elif x < 1200:
        print(5)
    elif x < 1400:
        print(4)
    elif x < 1600:
        print(3)
    elif x < 1800:
        print(2)
    elif x < 2000:
        print(1)
    else:
        pass


    return None

if __name__ == '__main__':
    main()
