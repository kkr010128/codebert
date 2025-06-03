import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import permutations
    from math import factorial

    N = int(readline())
    mat = []
    s = 0

    for _ in range(N):
        x, y = map(int, readline().split())
        mat.append([x, y])

    for per in permutations(range(N)):
        for i in range(N - 1):
            x1, y1 = mat[per[i]]
            x2, y2 = mat[per[i + 1]]
            s += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    print(s / factorial(N))


if __name__ == '__main__':
    main()
