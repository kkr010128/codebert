import numpy as np
from collections import Counter


def solve(string):
    n, *a = map(int, string.split())
    table = np.array([True] * (10**6 + 1))
    ma = max(a)
    for _a in a:
        if table[_a]:
            table[2*_a:ma + 1:_a]=False
    i = np.array([k for k,v in Counter(a).items() if v==1],dtype=np.int)
    return str(table[i].sum())


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
