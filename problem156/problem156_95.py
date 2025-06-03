#import numpy as np
#import math
#from decimal import *
#from numba import njit

#@njit
def main():
    X = int(input())

    p = []
    def pow5(n):
        nonlocal p
        if len(p) > n:
            return p[n]
        ans = pow(n,5)
        p += ans,
        return ans

    a = 0
    b = 0
    while True:
        if abs(X) + pow5(b) == pow5(a) or abs(X) - pow5(b) == pow5(a) :
            a5 = pow5(a)
            b5 = pow5(b)
            if X == a5 - b5:
                print(a,b)
            elif X == a5 + b5:
                print(a, -b)
            elif X == -a5 - b5:
                print(-a, b)
            else:
                print(-a, -b)
            return
        while abs(X) + pow5(b) > pow5(a):
            a += 1
            if abs(X) + pow5(b) == pow5(a) or abs(X) - pow5(b) == pow5(a) :
                a5 = pow5(a)
                b5 = pow5(b)
                if X == a5 - b5:
                    print(a,b)
                elif X == a5 + b5:
                    print(a, -b)
                elif X == -a5 - b5:
                    print(-a, b)
                else:
                    print(-a, -b)
                return
        a = 0
        b += 1

main()
