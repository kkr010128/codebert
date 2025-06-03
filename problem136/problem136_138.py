import numpy as np
import math
from decimal import *
#from numba import njit

def getVar():
    return map(int, input().split())
def getArray():
    return list(map(int, input().split()))
def getNumpy():
    return np.array(list(map(int, input().split())), dtype='int64')

def factorization(n):
    d = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            d.update({i: cnt})

    if temp!=1:
        d.update({temp: 1})

    if d==[]:
        d.update({n:1})

    return d

def main():
    N = int(input())
    d = factorization(N)
    count = 0

    for v in d.values():
        i = 1
        while(v >= i):
            v -= i
            i += 1
            count += 1
        
    print(count)


main()