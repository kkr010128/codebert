import math
import sys
from collections import Counter
import bisect
readline = sys.stdin.readline


def main():
    cnt = 0
    arg = 0
    x = int(readline().rstrip())
    for i in range(1000):
        cnt += 1
        arg += x
        arg %= 360
        if arg == 0:
            break
    print(cnt)


if __name__ == '__main__':
    main()
