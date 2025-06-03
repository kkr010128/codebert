#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    N = int(input())
    s = set()
    for _ in range(N):
        s.add(input())
    print(len(s))

main()
