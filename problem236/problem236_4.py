import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    [h, w, n] = [int(readline().rstrip()) for _ in range(3)]
    print(math.ceil(n/max(h, w)))


if __name__ == '__main__':
    main()
