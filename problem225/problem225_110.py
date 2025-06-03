import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


# sys.setrecursionlimit(10**5)


def main():
    h, a = geta(int)

    print((h + a - 1) // a)


if __name__ == "__main__":
    main()