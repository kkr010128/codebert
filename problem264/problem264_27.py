import math
import sys
readline = sys.stdin.readline


def main():
    m1, d1 = map(int, readline().rstrip().split())
    m2, d2 = map(int, readline().rstrip().split())
    print(1 if d2 == 1 else 0)


if __name__ == '__main__':
    main()
