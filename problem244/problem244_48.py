import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    K, X = map(int, readline().split())

    if 500 * K >= X:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
