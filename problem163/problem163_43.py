#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    S,W = map(int, input().split())
    if S <= W:
        print('unsafe')
    else:
        print('safe')    

main()
