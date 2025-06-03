import sys


def resolve():
    readline = sys.stdin.readline

    N, K = map(int, readline().split())
    P = sorted([int(x) for x in readline().split()])

    print(sum(P[:K]))

resolve()
