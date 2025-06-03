import sys
from math import atan, pi

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    a, b, x = map(int, readline().split())
    if x > a * a * b / 2:
        angle = atan(2 * (a * a * b - x) / a ** 3)
    else:
        angle = atan(a * b * b / (2 * x))

    print(angle / pi * 180)
    return


if __name__ == '__main__':
    main()
