import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A = int(readline())
    B = int(readline())

    print(6 - A - B)


if __name__ == '__main__':
    main()
