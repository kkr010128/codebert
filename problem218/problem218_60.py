import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    S = [readline().rstrip() for _ in range(n)]
    c = collections.Counter(S)
    keys = sorted(c.keys())
    maxS = c.most_common()[0][1]
    for key in keys:
        if c[key] == maxS:
            print(key)


if __name__ == '__main__':
    main()
