#!/usr/bin/env python3
import sys
import itertools
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    l = [i + 1 for i in range(N)]
    p = itertools.permutations(l, N)
    q = itertools.permutations(l, N)
    c = 1
    d = 1
    a = 0
    b = 0
    for i in p:
        x = 0
        for j in range(N):
            if i[j] == P[j]:
                x += 1
            else:
                break
        if x == N:
            a = c
            break
        c += 1
    for i in q:
        x = 0
        for j in range(N):
            if i[j] == Q[j]:
                x += 1
            else:
                break
        if x == N:
            b = d
            break
        d += 1
    ans = abs(a - b)
    print(ans)

if __name__ == '__main__':
    main()
