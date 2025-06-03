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

def main():
    t1,t2 = map(int,ipt().split())
    a1,a2 = map(int,ipt().split())
    b1,b2 = map(int,ipt().split())
    d1 = t1*(a1-b1)
    d2 = t2*(a2-b2)
    if d1*(d1+d2) > 0:
        print(0)
    elif d1+d2 == 0:
        print("infinity")
    else:
        dt = d1+d2
        if abs(d1)%abs(dt):
            print(abs(d1)//abs(dt)*2+1)
        else:
            print(abs(d1)//abs(dt)*2)

    return None

if __name__ == '__main__':
    main()
