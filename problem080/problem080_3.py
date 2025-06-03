#!python3

import sys
iim = lambda: map(int, sys.stdin.readline().rstrip().split())
from operator import sub

def resolve():
    it = map(int, sys.stdin.read().split())
    N = next(it)

    M = 10**9+1
    data = [[M, -M], [M, -M]]
    for x, y in zip(it, it):
        for i, x in enumerate([x+y, x-y]):
            for j, f in enumerate([min, max]):
                data[i][j] = f(data[i][j], x)

    print(max(map(lambda x: abs(sub(*x)), data)))



if __name__ == "__main__":
    resolve()
