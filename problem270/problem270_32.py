import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**5)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    d = {"SUN": 7, "MON": 6, "TUE": 5, "WED": 4, "THU": 3, "FRI": 2, "SAT": 1}

    print(d[gete()])


if __name__ == "__main__":
    main()