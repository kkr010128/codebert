import sys, math
from functools import lru_cache
import numpy as np
import heapq
from collections import defaultdict
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def sieve(n):
    res = [i for i in range(n)]

    i = 2
    while i*i < n:
        if res[i] < i:
            i += 1
            continue
        j = i*i
        while j < n:
            if res[j] == j:
                res[j] = i
            j += i
        i += 1

    return res

def factor(n, min_factor):
    res = set()
    while n > 1:
        res.add(min_factor[n])
        n //= min_factor[n]

    return res

def main():
    N = ii()
    A = np.array(list(mi()))

    m = max(A)
    s = sieve(m+1)
    d = defaultdict(bool)
    
    g = np.gcd.reduce(A)
    if g > 1:
        print('not coprime')
        return

    for a in A:
        f = factor(a, s)
        for v in f:
            if d[v]:
                print('setwise coprime')
                return
            d[v] = True

    print('pairwise coprime')



if __name__ == '__main__':
    main()
