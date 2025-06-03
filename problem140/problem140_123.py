import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    T = input()
    print(T.replace("?", "D"))


if __name__ == "__main__":
    main()
