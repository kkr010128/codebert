import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    (N, K) = map(int, input().split())
    A = np.array([0] + list(map(int, input().split())))

    B = [1]
    s = [True]*(N+1)
    s[1] = False
    nextTown = A[1]
    while s[nextTown]:
        B += nextTown,
        s[nextTown] = False
        nextTown = A[nextTown]
        
    B = np.array(B)
    loopIndex = np.where(B == nextTown)[0][0]
    loopLen = len(B) - loopIndex

    if K >= loopIndex:
        print(B[(K-loopIndex)%loopLen + loopIndex])
    else:
        print(B[K])

main()
