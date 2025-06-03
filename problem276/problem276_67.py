import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import accumulate

    N = int(readline())
    A = list(map(int, readline().split()))
    acc = list(accumulate(A))
    S = sum(A)

    ans = INF
    for first in acc:
        second = S - first
        ans = min(ans, abs(first - second))

    print(ans)


if __name__ == '__main__':
    main()
