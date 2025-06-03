import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *P = map(int, read().split())

    csum = [0]
    csum.extend(accumulate(P))

    ans = 0
    for i in range(N - K + 1):
        if ans < csum[i + K] - csum[i]:
            ans = csum[i + K] - csum[i]

    print((K + ans) / 2)
    return


if __name__ == '__main__':
    main()
