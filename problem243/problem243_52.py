import sys, math
from functools import lru_cache
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

def main():
    N = ii()
    s, t = [list(i) for i in zip(*[input().split() for i in range(N)])]
    t = list(map(int, t))
    k = s.index(input())
    print(sum(int(t[i]) for i in range(k+1, N)))



if __name__ == '__main__':
    main()