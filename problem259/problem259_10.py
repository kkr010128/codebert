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
    n,u,v = map(int,ipt().split())
    way = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,ipt().split())
        way[a].append(b)
        way[b].append(a)

    ta = [-1]*(n+1)
    tt = [-1]*(n+1)
    ta[v] = 0 #AOKI
    tt[u] = 0
    qa = queue.Queue()
    qt = queue.Queue()
    qt.put((0,u,-1))
    qa.put((0,v,-1))

    while not qa.empty():
        ti,pi,pp = qa.get()
        for i in way[pi]:
            if i == pp:
                continue
            if ta[i] == -1:
                ta[i] = ti+1
                qa.put((ti+1,i,pi))

    while not qt.empty():
        ti,pi,pp = qt.get()
        if ta[pi] <= ti:
            continue
        for i in way[pi]:
            if i == pp:
                continue
            if ta[i] > ti:
                tt[i] = ti+1
                qt.put((ti+1,i,pi))

    ma = 0
    for i in range(1,n+1):
        if tt[i] == -1:
            continue
        if ma < tt[i]+max(0,ta[i]-tt[i]-1):
            ma = tt[i]+max(0,ta[i]-tt[i]-1)
    print(ma)


    return

if __name__ == '__main__':
    main()
