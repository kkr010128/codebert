import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *D = map(int, read().split())

    csum = accumulate(D)
    ans = sum(s * d for s, d in zip(csum, D[1:]))
    print(ans)
    return


if __name__ == '__main__':
    main()
