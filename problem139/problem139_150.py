import math
import sys
readline = sys.stdin.readline


def main():
    h1, m1, h2, m2, k = map(int, readline().rstrip().split())
    print((max(0, (h2 - h1) * 60 + (m2 - m1) - k)))


if __name__ == '__main__':
    main()
