import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**5)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    a, b, c = geta(int)

    print("win" if sum([a, b, c]) <= 21 else "bust")


if __name__ == "__main__":
    main()