import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
import itertools
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    h,w,k = map(int,ipt().split())
    s = [list(map(int,list(input()))) for _ in [0]*h]
    '''
    sms = [[0]*w for _ in [0]*h]
    for i in range(w):
        for j in range(h):
            sms[j][i] = sms[j-1][i]+s[j][i]
        print(i)
    '''
    cmi = 10**18
    for i in range(2**(h-1)):
        pos = [0]*h
        for j in range(h-1):
            if (i >> j) & 1:
                pos[j+1] = pos[j]+1
            else:
                pos[j+1] = pos[j]
        cmii = pos[-1]
        si = [0]*h
        for jj in range(h):
            si[pos[jj]] += s[jj][0]
        if max(si) > k:
            continue
        f = True
        for j in range(1,w):
            if f:
                for ii in range(h):
                    if si[pos[ii]]+s[ii][j] > k:
                        cmii += 1
                        si = [0]*h
                        for jj in range(h):
                            si[pos[jj]] += s[jj][j]
                        if max(si) > k:
                            f = False
                        break
                    else:
                        si[pos[ii]]+=s[ii][j]
        if f and cmii < cmi:
            cmi = cmii
    print(cmi)
    return

if __name__ == '__main__':
    main()
