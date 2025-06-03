# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import product, accumulate, combinations, product
#import bisect
import numpy as np
#from copy import deepcopy
#from collections import deque
#from decimal import Decimal
#from numba import jit

INF = 1 << 50

def fill(h, H, W, S, MAP, marker):
    if not '#' in S[h]:
        return MAP, marker
    idxes = [i for i, s in enumerate(S[h]) if s == '#']
    upper = h
    for hh in range(h-1, 0 , -1):
        if MAP[hh][idxes[0]] == 0:
            upper = hh
        else:
            break
    down = h

    for hh in range(h+1, H+1):
        if '#' in S[hh]:
            break
        else:
            down = hh
    left = 1
    for idx in idxes:
        MAP[upper:down+1, left:idx+1] = marker
        marker += 1
        left = idx+1
    MAP[upper:down+1, left:W+1] = marker-1
    return MAP, marker



def run():
    H, W, K = map(int, input().split())
    S = ['0' * (W+2)]
    up = INF
    down = 0
    for i in range(1,H+1):
        s = input()
        if '#' in s:
            down = i
            if up == INF:
                up = i

        s = '0' + s + '0'
        S.append(s)
    S.append('0' * (W+2))
    #for s in S:
    #    print(s)

    MAP = np.zeros((H+2, W+2), dtype = np.int32)

    marker = 1
    for h in range(1, H+1):
        #print(h)
        MAP, marker = fill(h, H,W, S, MAP, marker)
        #print(MAP)


    for h in range(1, H+1):
        ans = [str(s) for s in MAP[h, 1:W+1]]
        print(' '.join(ans))

    #print(MAP)

if __name__ == "__main__":
    run()