#!/usr/bin/env python3

import statistics
import sys


def main():
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            sys.exit(0)
        print(statistics.pstdev([int(num) for num
                                in sys.stdin.readline().split()]))


if __name__ == '__main__':
    main()