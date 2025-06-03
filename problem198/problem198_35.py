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

def solve(d):
    if d == 1:
        return ['a']
    l = solve(d-1)
    rsl = []
    for w in l:
        m = ord(max(w))
        for i in range(ord('a'), m+2):
            rsl.append(w+chr(i))
    return rsl


def main():
    print(*solve(ii()), sep='\n')


if __name__ == '__main__':
    main()