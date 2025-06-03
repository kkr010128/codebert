import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n, m = map(int, readline().rstrip().split())
    a = list(map(int, readline().rstrip().split()))
    print(n - sum(a) if n - sum(a) >= 0 else -1)


if __name__ == '__main__':
    main()
