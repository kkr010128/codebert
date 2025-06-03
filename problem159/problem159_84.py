#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    X = int(input())
    a = 100
    count = 0
    while a < X:
        a += a//100
        count += 1
    print(count)   

main()
