import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    h = gete(int)
    w = gete(int)
    n = gete(int)

    if h < w:
        h, w = w, h

    print((h + n - 1) // h)


if __name__ == "__main__":
    main()