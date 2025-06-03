from sys import stdin
rs = stdin.readline
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))
from functools import reduce

def main():
    N, K = ril()
    A = ril()
    l = 1
    r = 1000000000
    while l < r:
        m = (l + r) // 2
        f = lambda i, j : i + (j - 1) // m
        k = reduce(f, A, 0)
        if k <= K:
            r = m
        else:
            l = m + 1
    print(r)

if __name__ == '__main__':
    main()
