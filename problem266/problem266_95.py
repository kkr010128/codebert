import sys, math
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(500000)
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

@lru_cache(maxsize=None)
def f(x):
    if x < 0:
        return False
    if (x%100==0) or (x%101==0) or (x%102==0) \
            or (x%103==0) or (x%104==0) or (x%105==0):
        return True
    return f(x-100) or f(x-101) or f(x-102) \
            or f(x-103) or f(x-104) or f(x-105)

def main():
    X = ii()
    print(1 if f(X) else 0)


if __name__ == '__main__':
    main()