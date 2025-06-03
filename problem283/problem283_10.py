from fractions import gcd
from datetime import date, timedelta
from heapq import*
import math
from collections import defaultdict, Counter, deque
import sys
from bisect import *
import itertools
import copy
sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7


def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res



def main():
    n = int(input())
    if n % 2 == 0:
        print((n - 1) // 2)
    else:
        print(n//2)

    
    

        
        
        
            

    
   


if __name__ == '__main__':
    main()
