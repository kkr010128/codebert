import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import permutations

    N = int(readline())
    P = tuple(map(int, readline().split()))
    Q = tuple(map(int, readline().split()))

    d = {x: i for i, x in enumerate(permutations(range(1, N + 1)))}

    print(abs(d[Q] - d[P]))


if __name__ == '__main__':
    main()
