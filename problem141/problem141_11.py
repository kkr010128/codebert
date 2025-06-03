import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n = int(ipt())
    a = [int(i) for i in ipt().split()]
    suma = sum(a)
    ans = 0
    can = 1
    for i,ai in enumerate(a):
        if ai > can:
            print(-1)
            exit()
        suma -= ai
        ans += can
        if (can-ai)*2 >= suma:
            can = suma
        else:
            can = (can-ai)*2

    print(ans)




    return

if __name__ == '__main__':
    main()
