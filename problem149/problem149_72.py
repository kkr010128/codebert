#!/usr/bin/env python3
import sys
from itertools import product
def input():
    return sys.stdin.readline()[:-1]

def main():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    for m in range(1, M + 1):
        s = 0
        for n in range(N):
            s += A[n][m]
        if s < X:
            print(-1)
            exit()

    # bit全探索
    # repeat=2だと(0,0), (0,1), (1,0), (1,1)になる
    ans = 10 ** 15
    for i in product([0,1], repeat=N):
        c = 0
        for m in range(1, M + 1):
            s = 0
            for n in range(N):
                if i[n] == 1:
                    s += A[n][m]
            if s >= X:
                c += 1
        if c == M:
            money = 0
            for n in range(N):
                if i[n] == 1:
                    money += A[n][0]
            ans = min(ans, money)
    print(ans)

if __name__ == '__main__':
    main()
