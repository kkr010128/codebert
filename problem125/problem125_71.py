import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x = int(readline())

    for i in range(1, 361):
        if (x * i) % 360 == 0:
            return print(i)


if __name__ == '__main__':
    main()
