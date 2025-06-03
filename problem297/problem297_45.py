#!/usr/bin/env python3
import sys
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(readline())
    print(math.ceil(N / 2) / N)


if __name__ == '__main__':
    main()
