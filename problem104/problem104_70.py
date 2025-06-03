import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    L, R, d = map(int, input().split())

    r = R // d
    l = (L - 1) // d
    print(r - l)


if __name__ == "__main__":
    main()
