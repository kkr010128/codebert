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
    n,m = map(int,ipt().split())
    a = [int(i) for i in ipt().split()]
    a.sort()
    maa = max(a)

    pn = [0]*(2*maa+1)
    pn[0] = n
    pa = 0
    for i in a:
        for j in range(pa+1,i+1):
            pn[j] = pn[pa]
        pn[i+1] = pn[pa]-1
        pa = i+1

    l = 0
    r = 2*maa
    while l < r:
        mid = l+(r-l+1)//2
        nm = 0
        for i in a:
            if mid <= i:
                nm += n
            else:
                nm += pn[mid-i]
        if nm >= m:
            l = mid
        else:
            r = mid-1

    pt = [0]*(2*maa+1)
    pp = maa+1
    for i in a[::-1]:
        for j in range(pp-1,i,-1):
            pt[j] = pt[pp]
        pt[i] = pt[pp]+i
        pp = i
    for j in range(pp-1,-1,-1):
        pt[j] = pt[pp]

    ans = 0
    sm = 0
    for i in a:
        sm += pn[max(0,l-i)]
        ans += pt[max(0,l-i)]+pn[max(0,l-i)]*i
    print(ans-l*(sm-m))
    return

if __name__ == '__main__':
    main()
