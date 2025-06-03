import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n = gete(int)
    d = tuple(geta(int))

    print(((sum(d)**2 - sum([di**2 for di in d]))) // 2)


if __name__ == "__main__":
    main()