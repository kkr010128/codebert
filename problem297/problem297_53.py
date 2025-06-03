import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())

    odd = 0
    for i in range(1, N + 1):
        if i % 2 == 1:
            odd += 1

    print(odd / N)


if __name__ == '__main__':
    main()
