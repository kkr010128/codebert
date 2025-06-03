import math
import sys
from collections import Counter
readline = sys.stdin.readline


def main():
    n, k = map(int, readline().rstrip().split())
    P = sorted(list(map(int, readline().rstrip().split())))
    print(sum(P[0: k]))


if __name__ == '__main__':
    main()
