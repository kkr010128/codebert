import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b = map(int, readline().split())

    print(str(min(a, b)) * max(a, b))


if __name__ == '__main__':
    main()
