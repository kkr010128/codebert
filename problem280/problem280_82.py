#!/usr/bin/env python3
import sys
import itertools
import math
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())

    l = [i for i in range(N)]
    p = [i for i in itertools.permutations(l, N)]
    d = 0
    for i in range(len(p)):
        t = p[i]
        for j in range(N - 1):
            d += math.sqrt(((x[t[j]] - x[t[j + 1]]) ** 2) + ((y[t[j]] - y
            [t[j + 1]])) ** 2)
    ans = d / math.factorial(N)
    print(ans)

if __name__ == '__main__':
    main()
