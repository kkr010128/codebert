import sys, math
from functools import lru_cache
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

def main():
    N = ii()
    x, y = i2(N)

    Mw = max(x[i]+y[i] for i in range(N))
    mw = min(x[i]+y[i] for i in range(N))
    Mz = max(x[i]-y[i] for i in range(N))
    mz = min(x[i]-y[i] for i in range(N))

    print(max(Mz-mz, Mw-mw))
    


if __name__ == '__main__':
    main()
