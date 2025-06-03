import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    H, A = map(int, readline().split())

    print((H + A - 1) // A)


if __name__ == '__main__':
    main()
