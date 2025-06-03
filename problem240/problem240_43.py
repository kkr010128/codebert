#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N, M = map(int, input().split())
    p = [0] * M
    S = [0] * M
    for i in range(M):
        p[i] , S[i] = map(str, input().split())
    for i in range(M):
        p[i] = int(p[i])

    AC = 0
    WA = 0
    l = [0] * N
    for i in range(M):
        if l[p[i] - 1] != 1:
            if S[i] == 'WA':
                l[p[i] - 1] -= 1
            elif S[i] == 'AC':
                WA += l[p[i] - 1] * (-1)
                l[p[i] - 1] = 1
                AC += 1
    print(AC, WA)

if __name__ == '__main__':
    main()
